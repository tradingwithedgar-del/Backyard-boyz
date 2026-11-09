"""Carry window outlines across the 30fps turntable video with a per-frame homography
(each side of a G-wagon is flat), then sample them at the 36 spin frames."""
import sys, json, cv2, numpy as np
D = sys.argv[1]
N = 285
def frame(i): return cv2.imread(f'{D}/gray/v{i+1:03d}.png', cv2.IMREAD_GRAYSCALE)
def area(p): return 0.5 * float(np.sum(p[:,0]*np.roll(p[:,1],-1) - np.roll(p[:,0],-1)*p[:,1]))

def track(seed_frame, polys, step, label):
    """polys: list of (k,2) arrays in 1920x1080 coords. Returns {frame: polys}."""
    polys = [np.array(p, np.float32) for p in polys]
    a0 = [area(p) for p in polys]
    out = {seed_frame: [p.copy() for p in polys]}
    i = seed_frame
    prev = frame(i)
    while True:
        j = i + step
        if j < 0 or j >= N: break
        cur = frame(j)
        allp = np.vstack(polys)
        x0, y0 = allp.min(0); x1, y1 = allp.max(0)
        w = x1 - x0
        mask = np.zeros_like(prev)
        mask[int(max(0, y0 - 30)):int(min(1080, y1 + 160)), int(max(0, x0 - 0.08*w)):int(min(1920, x1 + 0.08*w))] = 255
        pts = cv2.goodFeaturesToTrack(prev, 500, 0.01, 6, mask=mask)
        if pts is None or len(pts) < 20: print(label, 'stop: few features at', j); break
        nxt, st, _ = cv2.calcOpticalFlowPyrLK(prev, cur, pts, None, winSize=(31, 31), maxLevel=4)
        back, st2, _ = cv2.calcOpticalFlowPyrLK(cur, prev, nxt, None, winSize=(31, 31), maxLevel=4)
        good = (st[:,0] == 1) & (st2[:,0] == 1) & (np.linalg.norm(back - pts, axis=2)[:,0] < 1.0)
        if good.sum() < 15: print(label, 'stop: tracking lost at', j); break
        H, inl = cv2.findHomography(pts[good], nxt[good], cv2.RANSAC, 2.0)
        if H is None or inl.sum() < 12: print(label, 'stop: no homography at', j); break
        new = [cv2.perspectiveTransform(p.reshape(-1,1,2), H).reshape(-1,2) for p in polys]
        ratios = [area(n)/a for n, a in zip(new, a0)]
        if min(ratios) < 0.12: print(label, 'stop: edge-on at', j, [round(r,2) for r in ratios]); break
        polys = new; out[j] = [p.copy() for p in polys]; prev = cur; i = j
    print(label, 'tracked', len(out), 'frames', min(out), '-', max(out))
    return out

if __name__ == '__main__':
    seeds = json.load(open(sys.argv[2]))
    res = {}
    for name, s in seeds.items():
        for step in (1, -1):
            r = track(s['frame'], s['polys'], step, f'{name}{"+" if step>0 else "-"}')
            for f, ps in r.items():
                res.setdefault(name, {})[f] = [p.round(1).tolist() for p in ps]
    json.dump(res, open(sys.argv[3], 'w'))

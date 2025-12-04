# Addis 2025 Workshop

https://drive.google.com/drive/folders/1yszajARf4cwvPTxe2sEdruZXapNforKU?usp=sharing

# Erosion Studygroup
https://drive.google.com/drive/folders/1sc2Xr3CjfJY1NKfCcc0zhalnEh6B5MJC?usp=drive_link

# Link to erosion overleaf
https://www.overleaf.com/2774453841kkmkvpbmgtpy#22519f

# Mask code
```python
# Create mask
boundary_polygon = Path(np.column_stack([xb, yb]))
points = np.column_stack([X.ravel(), Y.ravel()])
mask_flat = boundary_polygon.contains_points(points)
mask = mask_flat.reshape(X.shape)
Z_masked = Z * mask
```

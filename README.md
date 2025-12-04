# Addis 2025 Workshop

https://drive.google.com/drive/folders/1yszajARf4cwvPTxe2sEdruZXapNforKU?usp=sharing

# Erosion Studygroup
https://drive.google.com/drive/folders/1sc2Xr3CjfJY1NKfCcc0zhalnEh6B5MJC?usp=drive_link

# Link to erosion overleaf
https://www.overleaf.com/2774453841kkmkvpbmgtpy#22519f

# Mask code
```python
from matplotlib.path import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path

# --- Load your data ---
X = np.loadtxt("../Addis2025_DEM/X_Abaya_DEM.txt")
Y = np.loadtxt("../Addis2025_DEM/Y_Abaya_DEM.txt")
Z = np.loadtxt("../Addis2025_DEM/Abaya_DEM.txt")

xb = np.loadtxt("../Addis2025_DEM/X_Abaya_catchment_boundary_try.txt")
yb = np.loadtxt("../Addis2025_DEM/Y_Abaya_catchment_boundary_try.txt")

# Create mask
boundary_polygon = Path(np.column_stack([xb, yb]))
points = np.column_stack([X.ravel(), Y.ravel()])
mask_flat = boundary_polygon.contains_points(points)
mask = mask_flat.reshape(X.shape)
Z_masked = Z * mask
```

import numpy as np
import plotly.graph_objects as go
import math
import json
from fastapi.responses import JSONResponse 
# B for Magnetic field
# A for Area
# theta for Angle

def visualize_inputs(B, A, theta, angle_unit = "Radians"):
    if angle_unit == "Degrees":
        theta = theta * (np.pi/180)

    flux =  B * A * np.cos(theta)
    # print(f"B = {B}")
    # print(f"A = {A}")
    # print(f"theta = {theta}")
    # print(f"cosine = {math.cos(theta)}")
    # print(f"flux = {flux}")

    x, y = np.meshgrid(np.linspace(-3,3,5), np.linspace(-3,3,5))
    z = np.zeros_like(x)
    
    u = np.zeros_like(x)
    v = np.zeros_like(y)
    w = np.ones_like(z) * B 


    plane_size = np.sqrt(A)

    xx, yy = np.meshgrid(np.linspace(-plane_size, plane_size, 2),
                        np.linspace(-plane_size, plane_size, 2))

    zz= xx * 0 + yy *np.tan(theta)
    fig = go.Figure()

    fig.add_trace(go.Cone(x=x.flatten(), y=y.flatten(), z=z.flatten(), 
                        u=u.flatten(), v=v.flatten(), w=w.flatten(),
                        sizemode="absolute", sizeref=2,
                        colorscale="Blues",showscale= False, name="Magnetic Field"))

    fig.add_trace(go.Surface(x=xx, y=yy, z=zz,
                        opacity=0.6, colorscale="YlOrRd",
                        showscale=False,
                        name="Surface"))

    fig.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[np.max(zz) +1],
        text = [f"<b>Flux = {flux:.4f} Wb</b>" ],
        mode="text",
        showlegend=False
    ))              

    fig.update_layout(
        title=f"Magnetic Flux Visualization",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z",
            aspectratio=dict(x=1, y=1,z=1)
        )
    )

    # fig_json = json.loads(fig.to_plotly_json())
    return fig.to_plotly_json()


# visualize_inputs(B=0.8, A=1.2, theta=0.7) 
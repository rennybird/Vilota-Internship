import open3d as o3d
import numpy as np
import time

def create_camera_wireframe():
    points = np.array([                             #Define the coordinates of the camera wireframe
        [0, 0, 0],  
        [-0.5, -0.5, -1],  
        [0.5, -0.5, -1],  
        [0.5, 0.5, -1],  
        [-0.5, 0.5, -1],  
    ])
    lines = np.array([                              #Define the lines between the coordinate points
        [0, 1], [0, 2], [0, 3], [0, 4],  
        [1, 2], [2, 3], [3, 4], [4, 1],  
    ])
    line_set = o3d.geometry.LineSet(                #Create the line set
        points=o3d.utility.Vector3dVector(points),
        lines=o3d.utility.Vector2iVector(lines),
    )
    return line_set

def animate_camera_wireframe(vis, camera_wireframe, num_frames=120, radius=2):
    for frame in range(num_frames):         #Loop through each frame
        angle = 2 * np.pi * (frame / float(num_frames))     #Calculate the angle for the current frame
        
        # Create 4x4 transformation matrix
        transformation_matrix = np.eye(4)
        # Set roation matrix around y axis
        transformation_matrix[:3, :3] = o3d.geometry.get_rotation_matrix_from_zyx((0, angle, 0))
        # Set translation in x and z axis to be a circle movement
        transformation_matrix[0, 3] = radius * np.sin(angle)
        transformation_matrix[2, 3] = radius * np.cos(angle)

        #Apply the transformation 
        camera_wireframe.points = o3d.utility.Vector3dVector(
            np.asarray(create_camera_wireframe().points).dot(transformation_matrix[:3, :3].T) + transformation_matrix[:3, 3]
        )
        
        
        # Update the geometry in Open 3D visualizer
        vis.update_geometry(camera_wireframe)
        vis.poll_events()
        vis.update_renderer()
        time.sleep(0.05)

def main():
    camera_wireframe = create_camera_wireframe() #Create wire frame model
    vis = o3d.visualization.Visualizer() # Start the visualizer
    vis.create_window() #Create the window
    vis.add_geometry(camera_wireframe) #Add wireframe to  visualizer
    animate_camera_wireframe(vis, camera_wireframe) #Animate the wireframe
    vis.destroy_window() #Close window

if __name__ == "__main__":
    main()

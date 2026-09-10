
import vtk

def main():

    reader = vtk.vtkSTLReader()
    reader.SetFileName('/Users/megana/Downloads/skull file corrected.stl')
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)


    renderer.AddActor(actor)
    renderer.SetBackground(1,1,1)
    renderWindow.Render()
    renderWindowInteractor.Start()





#note, the code will not work if the indentation below is not correct. the indentation below is correct but if the if 
# statement containing the main is actually inside main, the code will not run and no error will be shown. 
if __name__ == "__main__":
        main()

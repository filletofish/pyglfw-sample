import glfw
import OpenGL.GL as gl

rotation_angle = 0
d_x = 0

class Color():
     red = 1
     green = 0
     blue = 0

color = Color()

# KEY_DOWN = 264
# KEY_UP = 265

def on_key(window, key, scancode, action, mods):
    global d_x
    global color
    if action == glfw.PRESS:
            # ESC to quit
            if key == glfw.KEY_ESCAPE:
                glfw.set_window_should_close(window,1)
            elif key == glfw.KEY_UP:
                d_x += 0.1
            elif key == glfw.KEY_DOWN:
                d_x += -0.1
            elif key == glfw.KEY_SPACE:
                color.red += color.blue
                color.blue = color.red - color.blue
                color.red = color.red - color.blue


def main():
    global rotation_angle
    global d_x

    # Initialize the library
    if not glfw.init():
        print("library is not initialized")
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    print(glfw.__version__)



    glfw.set_key_callback(window, on_key)
    #glfw.set_mouse_button_callback(window, on_mouse)
    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL

        width, height = glfw.get_framebuffer_size(window)
        ratio = width / float(height)

        rotation_angle += 0.1

        # Set viewport
        gl.glViewport(0, 0, width, height)
        # Clear color buffer
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        # Select and setup the projection matrix
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(-ratio, ratio, -1, 1, 1, -1)
        # Select and setup the modelview matrix
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()

        gl.glRotatef(rotation_angle, 0, 0, 1)
        gl.glBegin(gl.GL_POLYGON)
        gl.glColor3f(color.red, color.green, color.blue)
        gl.glVertex3f(-0.5 + d_x, -0.5, 0)
        gl.glColor3f(color.red, color.green, color.blue)
        gl.glVertex3f(-0.5 + d_x, +0.5, 0)
        gl.glColor3f(color.red, color.green, color.blue)
        gl.glVertex3f( 0.5 + d_x, +0.5, 0)
        gl.glColor3f(color.red, color.green, color.blue)
        gl.glVertex3f( 0.5 + d_x, -0.5, 0)
        gl.glEnd()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    # terminating the whole proccess
    glfw.terminate()


if __name__ == "__main__":
    main()

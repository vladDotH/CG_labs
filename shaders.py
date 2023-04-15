from OpenGL import GL as gl


def readShader(file):
    return open(file, 'r').read()


def createShader(shader_type, file):
    shader = gl.glCreateShader(shader_type)
    gl.glShaderSource(shader, readShader(file))
    gl.glCompileShader(shader)
    return shader


def createWaveProgram():
    vertex = createShader(gl.GL_VERTEX_SHADER, './wave.vert')
    fragment = createShader(gl.GL_FRAGMENT_SHADER, './wave.frag')
    waveProgram = gl.glCreateProgram()
    gl.glAttachShader(waveProgram, vertex)
    gl.glAttachShader(waveProgram, fragment)
    gl.glLinkProgram(waveProgram)
    return waveProgram

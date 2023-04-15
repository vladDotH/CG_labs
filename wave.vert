uniform float length;
uniform float amplitude;

varying vec4 vertex_color;

void main() {
    vec4 pos = gl_Vertex;
    pos.y = pos.y + sin(pos.x * 3.14 * length) * amplitude;
    gl_Position = gl_ModelViewProjectionMatrix * pos;
    vertex_color = gl_Color;
}
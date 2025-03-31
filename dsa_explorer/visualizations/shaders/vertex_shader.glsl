#version 330

in vec2 in_position;        // Input vertex position
uniform mat4 transform;     // Transformation matrix

void main() {
    // Apply the transformation to the vertex position
    gl_Position = transform * vec4(in_position, 0.0, 1.0);
}
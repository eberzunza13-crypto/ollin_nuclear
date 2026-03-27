cat > core/__init__.py << 'EOF'
"""
Ollin Nuclear - Núcleo del sistema
La soberanía tecnológica en código.
"""

from .anthelion_physics import AnthelionPhysics
from .ometeotl_guard import OmeteotlGuard
from .noosphere_auth import NoosphereAuth

__version__ = "3.0.0"
__all__ = ["AnthelionPhysics", "OmeteotlGuard", "NoosphereAuth"]
EOF

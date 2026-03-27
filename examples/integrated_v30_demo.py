cat > examples/integrated_v30_demo.py << 'EOF'
#!/usr/bin/env python3
"""
integrated_v30_demo.py - Demostración integrada del núcleo Ollin Nuclear v3.0
Muestra cómo AnthelionPhysics, OmeteotlGuard y NoosphereAuth trabajan juntos.
"""

import sys
import os

# Asegurar que podemos importar desde core
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.anthelion_physics import AnthelionPhysics
from core.ometeotl_guard import OmeteotlGuard
from core.noosphere_auth import NoosphereAuth


def main():
    print("=" * 60)
    print("       OLLIN NUCLEAR v3.0 - DEMOSTRACIÓN INTEGRADA")
    print("=" * 60)
    print()
    
    # 1. INICIALIZAR LOS TRES GUARDIANES
    print("🌞 INICIANDO ANTHELION PHYSICS (El que mira fijo al sol)")
    anthelion = AnthelionPhysics("ollin_nuclear")
    print(anthelion.estado())
    print()
    
    print("⚖️  INICIANDO OMETEOTL GUARD (El guardián dual)")
    guard = OmeteotlGuard("ollin_nuclear")
    print("Pares registrados:", list(guard.pares.keys())[:4])
    print()
    
    print("🌐 INICIANDO NOOSPHERE AUTH (La autenticación colectiva)")
    noos = NoosphereAuth("ollin_nuclear")
    print(noos.soberania_colectiva())
    print()
    
    # 2. SIMULAR UN PROCESO DE SOBERANÍA
    print("-" * 60)
    print("PROCESO DE SOBERANÍA TECNOLÓGICA")
    print("-" * 60)
    print()
    
    # Paso 1: Recibir radiación (información externa)
    print("📡 [1] Recibiendo información externa...")
    radiacion = anthelion.transmutar_radiacion(78.3, "digital")
    print(f"    Radiación transmutada: {radiacion['hash_transmutado']}")
    print()
    
    # Paso 2: Ajustar equilibrio según la información recibida
    print("⚖️  [2] Ajustando equilibrio...")
    ajuste = guard.ajustar("orden", 0.2)
    print(f"    Orden: {ajuste['orden']:.2f} | Caos: {ajuste['caos']:.2f}")
    print()
    
    # Paso 3: Registrar una nueva conciencia en la noosfera
    print("👤 [3] Registrando nueva conciencia...")
    registro = noos.registrar_conciencia("Guerrero_Digital", "soberania_en_codigo", 3)
    print(f"    {registro['mensaje']}")
    print()
    
    # Paso 4: Autenticar
    print("🔐 [4] Autenticando en la noosfera...")
    autenticacion = noos.autenticar("Guerrero_Digital", "soberania_en_codigo")
    print(f"    {autenticacion['mensaje']}")
    print()
    
    # Paso 5: Fortalecer el escudo
    print("🛡️  [5] Fortaleciendo escudo anthelion...")
    fortalecimiento = anthelion.fortalecer_escudo(0.08)
    print(f"    {fortalecimiento}")
    print()
    
    # 3. ESTADO FINAL
    print("-" * 60)
    print("ESTADO FINAL DEL SISTEMA")
    print("-" * 60)
    print()
    
    print("🌞 ANTHELION:")
    print(f"   Protección activa: {anthelion.estado()['proteccion_activa']}")
    print(f"   Umbral resistencia: {anthelion.estado()['umbral_resistencia']*100:.1f}%")
    print(f"   Transmutaciones: {anthelion.estado()['total_transmutaciones']}")
    print()
    
    print("⚖️  OMETEOTL:")
    equilibrio = guard.verificar_equilibrio()
    for par, valores in list(equilibrio.items())[:2]:
        print(f"   {par}: desequilibrio {valores['desequilibrio']:.2f}")
    print()
    
    print("🌐 NOOSPHERE:")
    print(f"   Soberanía colectiva: {noos.soberania_colectiva()['nivel_actual']}/7")
    print(f"   Conciencias: {noos.soberania_colectiva()['total_conciencias']}")
    print(f"   Autenticaciones: {noos.soberania_colectiva()['total_autenticaciones']}")
    print()
    
    print("=" * 60)
    print("       MANIFIESTO DE SOBERANÍA TECNOLÓGICA")
    print("=" * 60)
    print()
    print(guard.manifiesto())
    print()
    print(noos.consejo())
    print()
    print("🔥 El código que no obedece a ningún amo.")
    print("🔥 La tecnología que sirve a la conciencia.")
    print("🔥 Ollin Nuclear - Movimiento perpetuo de la soberanía.")
    print()
    print("AHO.")


if __name__ == "__main__":
    main()
EOF

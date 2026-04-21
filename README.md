# Documentación del Módulo Seguimiento de Clientes - Odoo 19

## Descripción
Módulo personalizado para gestionar el seguimiento de clientes en Odoo 19.

## Requisitos
- Odoo 19.0
- Dependencias: base, contacts

## Estructura del módulo

```
seguimiento_clientes/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── seguimiento.py
├── views/
│   └── seguimiento_views.xml
└── security/
    └── ir.model.access.csv
```

## Modelo: seguimiento.cliente

| Campo | Tipo | Descripción |
|-------|------|-----------|
| nombre | Char | Nombre o asunto del seguimiento |
| cliente_id | Many2one | Relación con res.partner |
| fecha | Date | Fecha del seguimiento |
| estado | Selection | Pendiente / Realizado |
| notas | Text | Observaciones |

## Vistas incluidas
- **Vista lista** (`list`): Visualización de registros
- **Vista formulario** (`form`): Crear/editar seguimientos
- **Vista búsqueda** (`search`): Filtro de pendientes

## Funcionalidad
- Botón "Marcar Realizado" cambia el estado del seguimiento
- Filtro por defecto para mostrar solo pendientes

## Instalación
1. Copiar la carpeta `seguimiento_clientes` a `/opt/odoo/custom_addons/`
2. Asignar permisos: `sudo chown -R odoo:odoo /opt/odoo/custom_addons/seguimiento_clientes/`
3. Reiniciar Odoo: `sudo systemctl restart odoo`
4. Actualizar módulos en Odoo
5. Instalar "Seguimiento de Clientes"

## Acceso
- Menú: **Ventas > Clientes > Seguimiento**

## Errores comunes y soluciones

| Error | Solución |
|-------|---------|
| Permission denied en static | `sudo chown -R odoo:odoo /opt/odoo/custom_addons/seguimiento_clientes/` |
| tree no compatible | Usar `list` en lugar de `tree` en Odoo 19 |
| Manifest no leído | Simplificar `__manifest__.py` al formato mínimo |
| Módulo no aparece en Apps | Verificar `application: True` en manifest |

## Autor
Noel Gonzalez - UF1889E1

## Licencia
LGPL-3
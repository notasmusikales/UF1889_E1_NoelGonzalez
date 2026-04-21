# Lógica de funcionamiento del módulo seguimiento_clientes

## 1. Objetivo
Este módulo permite registrar seguimientos comerciales asociados a clientes en Odoo 19.

## 2. Modelo creado
Se ha creado el modelo `seguimiento.cliente` con los siguientes campos:
- `nombre`: guarda el nombre o asunto del seguimiento.
- `cliente_id`: relaciona el seguimiento con un cliente de Odoo.
- `fecha`: almacena la fecha del seguimiento.
- `estado`: indica si el seguimiento está pendiente o realizado.
- `notas`: permite añadir observaciones.

## 3. Vistas creadas
Se ha desarrollado:
- una vista lista (`list`) para visualizar varios registros.
- una vista formulario (`form`) para crear y editar seguimientos.
- una vista de búsqueda (`search`) con filtro de pendientes.

## 4. Funcionalidad implementada
Se ha implementado el método `action_marcar_realizado`, que cambia el estado del seguimiento a `realizado` al pulsar un botón en el formulario.

## 5. Filtro aplicado
Se ha añadido un filtro para mostrar únicamente los seguimientos con estado `pendiente`.

## 6. Pruebas realizadas
- instalación correcta del módulo
- creación de registros
- visualización en lista y formulario
- cambio de estado mediante botón
- filtrado de pendientes

## 7. Incidencias y correcciones
- Error de permisos en carpeta static: corregido con `chown -R odoo:odoo`
- Error de sintaxis XML en `__manifest__.py`: simplificado a formato mínimo
- Error de `tree` vs `list` en Odoo 19: corregido usando `list`
- Error de manifest no leído: causado por datos corruptos en base de datos
- Módulo no aparecía en menú: corregido usando parent en sales_team.menu_sales

## 8. Campos del modelo

| Campo | Tipo | Descripción | Requerido |
|-------|------|-----------|----------|
| nombre | Char | Nombre del seguimiento | Sí |
| cliente_id | Many2one | Cliente (res.partner) | Sí |
| fecha | Date | Fecha del seguimiento | Sí |
| estado | Selection | Pendiente/Realizado | Sí |
| notas | Text | Observaciones | No |
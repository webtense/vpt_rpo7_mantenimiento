# -*- coding: utf-8 -*-
{
    'name': 'RPO 7.0 Mantenimiento',
    'version': '16.1.1',
    'category': 'Maintenance',
    'summary': 'Gestión integral de mantenimiento para hoteles',
    'description': """
        Este módulo proporciona una gestión integral del mantenimiento,
        cubriendo desde inspecciones obligatorias hasta tareas diarias.
        Funciones principales:
        - Creación y asignación de tareas de mantenimiento.
        - Registro de inspecciones obligatorias y preventivas.
        - Control de repuestos y proveedores autorizados.
        - Configuración de planes de mantenimiento por instalación.
    """,
    'author': 'Andrés Sánchez',
    'website': 'https://www.boitaullresort.com',
    'depends': ['base', 'mail'],
    'data': [
#        'security/ir.model.access.csv',
        'views/action_dashboard_views.xml',
        'views/menu_views.xml',
        'views/libro_direccion_views.xml',
        'views/inspecciones_obligatorias_views.xml',
        'views/plan_mantenimiento_views.xml',
        'views/mantenimiento_preventivo_views.xml',
        'views/inspecciones_sci_views.xml',
        'views/combustion_calderas_views.xml',
        'views/planos_hoteles_views.xml',
        'views/checklist_tareas_views.xml',
        'views/servicios_habitaciones_views.xml',
        'views/proveedores_autorizados_views.xml',
        'views/control_detectores_views.xml',
        'views/inspecciones_extintores_views.xml',
        'views/tareas_exteriores_views.xml',
    ],
    'images': ['static/description/inspecciones.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}

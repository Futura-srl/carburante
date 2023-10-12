{
    'name': 'carburante',
    'version': '16',
    'author': "Luca Cocozza",
    'application': True,
    'description': "Gestione dei rifornimenti relativi alla flotta aziendale.",
    'depends': ['hr', 'fleet', 'gtms_fleet_organization', 'fleet_limited_traffic_zone', 'gtms_fleet_service_with_deduction', 'fleet_replacement',],
    'data': [
        # # Settaggi per accesso ai contenuti
        'data/ir.model.access.csv',
        # # Caricamento delle view,
        # 'view/hr_update.xml',
        'view/fleet_fuel_view.xml',
        # Menu
        'view/menu.xml',
    ],
}

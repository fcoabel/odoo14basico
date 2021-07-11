## Ejemplo básico odoo 14

### Creación de un módulo basico en Odoo 14.

En la carpeta instalacionodoo se  encuentra un script para instalarlo en Linux.

Nos posicionamos en /opt/osoo/odoo y ejecutamos

~~~~
sudo ./odoo-bin scaffold ejemplo ./addons/
~~~~

Siendo ejemplo el nombre del módulo. 

### Creación de un modelo.
Crearemos el siguiente modelo:

![](images/modelobasedatos.png)

 En models/models.py añadimos la defininón del nuevo modelo:
~~~~

from odoo import models, fields, api

class persona(models.Model):
	_name = 'ejemplo.persona'
	_description = 'model persona'

	name = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	telefono = fields.Char(string='Teléfono',required=True)
~~~~

name es el nombre del campo que se utilizará como índice, siempre se debe llamar así.
Ahora vamos a comprobar el funcionamiento del modelo creado.
Cada vez que se modifique un fichero python, deberemos reiniar Odoo.

~~~~
Para ver el fichero log de Odoo:
tail -f /var/log/odoo/odoo-server.log

Reiniciar:
sudo /etc/init.d/odoo restart 
~~~~

Activamos modo desarrollador:

Ajustes -> Herramientas de desarrollador -> Activar el modo de desarrollador

Actualizamos la lista de aplicaciones:

Aplicaciones -> Actualizar lista de aplicaciones

Buscamos nuestro módulo y los instalamos. Una vez instalado el módulo, iremos a:
Ajustes -> Técnico -> Estructura de la base de datos -> modelos, si todo funciona correctamente, estará nuestro modelo (ejemplo.persona) con los campos creados 
tamnién tendrá otros campos internos de Odoo.

![](images/modelo.png)

###Creación de vistas
Añadimos al fichero views/views.xml:
~~~~

    <!-- Vistas de persona-->

    <record model="ir.ui.view" id="ejemplo.persona_list_view">
      <field name="name">ejemplo.persona.view.tree</field>
      <field name="model">ejemplo.persona</field>
      <field name="arch" type="xml">
        <tree>
          <field name="name"/>
          <field name="nombre"/>
          <field name="telefono"/>
          <field name="fecha_nacimiento"/>
        </tree>
      </field>
    </record>

<!-- search -->

    <record model="ir.ui.view" id="ejemplo.persona_search_view">
      <field name="name">ejemplo.persona.view.search</field>
      <field name="model">ejemplo.persona</field>
      <field name="arch" type="xml">
        <search>
          <field name="name"/>
          <field name="nombre"/>
          <field name="telefono"/>
          <group>
            <filter name="group_by_nombre" string="nombre" context="{'gropup_by':'nombre'}" />
          </group>
        </search>
      </field>
    </record>

    
    <!-- form -->
    
    <record model="ir.ui.view" id="ejemplo.persona_form_view">
      <field name="name">ejemplo.persona.view.form</field>
      <field name="model">ejemplo.persona</field>
      <field name="arch" type="xml">
        <form string="Información persona">
          <sheet>
            <div class="oe_title">
              <h1>
                DNI <field name="name" placeholder="dni"/>
              </h1>
            </div>
            <group>
              <group>
                <separator string="Datos"/>
                <field name="nombre" placeholder="nombre"/>
                <field name="telefono"/>
                <field name="fecha_nacimiento"/>
              </group>
            </group>
          </sheet>
        </form>
      </field>

    </record>



<!-- calendar -->

    <record model="ir.ui.view" id="ejemplo.persona_calendar_view">
      <field name="name">ejemplo.persona.view.calendar</field>
      <field name="model">ejemplo.persona</field>
      <field name="arch" type="xml">
        <calendar string="Fecha de nacimiento" date_start="fecha_nacimiento" color="nombre" mode="month">
          <field name="name"/>
          <field name="nombre"/>
          <field name="telefono"/>
        </calendar>
      </field>
    </record>




    <!-- Definición de menús-->

    <!-- actions opening views on models -->

    <record model="ir.actions.act_window" id="ejemplo.persona_action_window">
      <field name="name">Personas</field>
      <field name="res_model">ejemplo.persona</field>
      <field name="view_mode">tree,form,calendar</field>
    </record>

    <menuitem name="ejemplo" id="ejemplo.menu_root"/>
    <menuitem name="Personas" id="ejemplo.menu_persona" parent="ejemplo.menu_root"/>
    <menuitem name="List" id="ejemplo.menu_persona_list" parent="ejemplo.menu_persona"
              action="ejemplo.persona_action_window"/>

~~~~

Debido a los modelos de seguridad  no, nos aparece el menú de nuestro módulo, este problema lo solucionaremos más adelante, 
para poder visualizarlo deberemos ser superusuarios (icono bug-> convertirse en superusuario), ya si nos aparecerá nuestro módulo.



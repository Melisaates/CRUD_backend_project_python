from leanapi.server import Modules
from .routes.brand import brand
from .routes.city import city
from .routes.dealer import dealer
from .routes.neighboor import neighboor
from .routes.product.product import Product
from .routes.district import district

modules = Modules.controllers([city])
modules= Modules.controllers([Product])

modules= Modules.controllers([dealer])
modeles = Modules.controllers([district])
modeles = Modules.controllers([neighboor])
modeles = Modules.controllers([brand])


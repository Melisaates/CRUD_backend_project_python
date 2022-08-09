from leanapi.path import controller
from leanapi.server import router
from sqlraw.sqlraw import SqlRaw
from fastapi import status
from starlette.responses import JSONResponse
from api.config import Config


@controller("app", router)
class Product:
    @router.get("/products/{product_id}", status_code=status.HTTP_200_OK,tags=["Product"], summary="product listesi")
    def get_product(self,product_id:int):
        sql = SqlRaw.paths(["api/routes/product/model"])
        sql.load("product.sql").connect(Config.conn)
        list = sql.fetchone({"product_id":product_id})
        print(list)
        if list:
            return list
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"message": "product bulunamadı"})

from leanapi.path import controller
from leanapi.server import router
from pydantic import json
from sqlraw.sqlraw import SqlRaw
from fastapi import status, Body
from starlette.responses import JSONResponse
from api.config import Config


@controller("app", router)
class Dealer:
    @router.get("/dealer/{dealer_id}", status_code=status.HTTP_200_OK, tags=["dealer"])
    def get_dealer(self, dealer_id: int):
        sql = SqlRaw.paths(["api/routes/dealer/model"])
        sql.load("dealer.sql").connect(Config.conn)
        list = sql.fetchone({"dealer_id": dealer_id})
        if list:
            return list
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"message": "dealer not found"})

    @router.get("/dealer/{city_id}", status_code=status.HTTP_200_OK, tags=["dealer info"])
    def get_new_dealer(self, city_id: int):
        sql = SqlRaw.paths(["api/routes/dealer/model"])
        sql.load("new_dealer.sql").connect(Config.conn)
        list = sql.fetchall({"city_id": city_id})
        if list:
            return list
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"message": "city id not found"})

    # @router.post("/dealer/", status_code=status.HTTP_200_OK)
    # def create_dealer(self, id: int = Body(..., embed=True), dealer_name: str = Body(..., embed=True),
    #                   dealer_code: str = Body(..., embed=True),
    #                   neighborhood_id: int = Body(..., embed=True),
    #                   district_id: int = Body(..., embed=True),
    #                   city_id: int = Body(..., embed=True),
    #                   working_hours: str = Body(..., embed=True),
    #                   is_active: bool = Body(..., embed=True),
    #                   qrcode: str = Body(..., embed=True),
    #                   info: str = Body(..., embed=True),
    #                   image: str = Body(..., embed=True),
    #                   payment_info: str = Body(..., embed=True),
    #                   table_is_active: bool = Body(..., embed=True),
    #                   reservation_is_active: bool = Body(..., embed=True),
    #                   marketplaces_is_active: bool = Body(..., embed=True)):
    #
    #     sql = SqlRaw.paths(["api/routes/dealer/model"])
    #     sql.load("dealer_post.sql").connect(settings.conn)
    #
    #     ll = sql.fetchone({"id": id, "dealer_name": dealer_name, "dealer_code": dealer_code,
    #                        "neighborhood_id": neighborhood_id, "district_id": district_id, "city_id": city_id,
    #                        "working_hours": working_hours, "is_active": is_active, "qrcode": qrcode, "info": info,
    #                        "image": image, "payment_info": payment_info, "table_is_active": table_is_active,
    #                        "reservation_is_active": reservation_is_active,
    #                        "marketplaces_is_active": marketplaces_is_active})
    #     print(ll)

    @router.put("/dealer/{dealer_id}", status_code=status.HTTP_200_OK, tags=["update_dealer"])
    def update_dealer(self, dealer_id: int, dealer_code: str = Body(..., embed=True)):

        sql = SqlRaw.paths(["./api/routes/dealer/model"])
        sql.load("dealer_update.sql").connect(Config.conn)
        a = sql.fetchall({"dealer_id": dealer_id, "dealer_code": dealer_code})
        return "success"

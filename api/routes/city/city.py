from leanapi.path import controller
from leanapi.server import router
from sqlraw.sqlraw import SqlRaw
from fastapi import status
from starlette.responses import JSONResponse
from api.config import Config


@controller("app",router)
class City:
    @router.get("/Products/",status_code=status.HTTP_200_OK,tags=["city"],summary="list the city")
    def get_city(self):
        sql=SqlRaw.paths(["api/routes/city/Model"])
        sql.load("city.sql").connect(Config.conn)
        list=sql.fetchall()

        if list:
            return list
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"message":"list not found"})
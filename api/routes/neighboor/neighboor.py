from leanapi.path import controller
from leanapi.server import router
from fastapi import status, Body
from starlette.responses import JSONResponse
from api.config import Config
from sqlraw.sqlraw import SqlRaw

@controller("app",router)
class Neighboor:
    @router.get("/neighboors/",tags=["neighboor"],status_code=status.HTTP_200_OK)
    def get_neighboor(self):
        sql=SqlRaw.paths(["api/routes/neighboor/model"])
        sql.load("neighboor.sql").connect(Config.conn)
        list=sql.fetchall()

        if list:
            return list
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"message":"list not found"})
    @router.post("/neighboors/")
    def create_neighboor(self,district_id:int=Body(...,embed=True),name:str=Body(...,embed=True)):
        sql = SqlRaw.paths(["api/routes/neighboor/model"])
        sql.load("neighboor_insert.sql").connect(Config.conn)

        return "successful"
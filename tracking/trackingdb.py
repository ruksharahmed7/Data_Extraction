import dataExtraction.database.connectdb as db

def get_project_name(project_id):
    project_name=db.fatch(project_id)
    return project_name

def insertnewproject(project_id,project_name):
    print("inserting")
    db.insert(project_id,project_name)
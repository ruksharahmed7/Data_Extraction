# Project Title

***Database Design for Capacity Enhancement of NEC-ECNEC & ordination Wing by Introducing Digital Database and Archive System***
# Module Name
***Auto-parser*** to extract meta-data from different unstructured sources

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
Python 3.4 or later
```

### Installing

Create a virtual environment by using virtualenv or venv. Activate environment and Install required package in this environment by using pip. 

```
source /pathtoenv/bin/activate
pip install requirements.txt
```

Or easily run from project directory

```
python setup.py
```

## API Documentation

* ### File Conversion
This API convert docx file in pdf format.
```
Route: /file_convert
Method: [POST]
Input: folder_name
       file_name

Output: Response message: Already converted or Successfully converted
```

* ### Data Extraction
This API extract define meta-data from a specific file. Source file can be DPP(Development Project Proposal), DPP Summary- Brief or Main Summary, Meeting Minute.
Format of file must be docx type.
```
Route: /data_extraction
Method: [POST]
Input: folder_name
       file_name
       project_id
       project_name

Output: JSON response
```
***JSON response will be a list of dictionary and contains:***

#### DPP json response:
```
[
  {
    "approval_date": "", "cabinet_division_map":, "cost_unit": "", "end_date": "", "end_month": "","end_year": "","executing_agency": "","gob_cost": "","gob_cost_lakh": ,"other_cost": "","other_cost_lakh": ,"own_fund": "","own_fund_lakh": ,"pa_cost": "","pa_cost_lakh": ,"planning_division": "","project_activity": "","project_cost": "","project_cost_lakh": ,"project_id": "","project_location": [],
    "project_location_tab": [
      {
        "district": "",
        "division": "",
        "upzila": ""
      },
    ],
    "project_name": "","project_name_english": "","project_purpose": "","revised_end_date": "","revised_end_month": ,"revised_end_year": ,"revised_gob_cost": "","revised_gob_cost_lakh": ,"revised_other_cost": "","revised_other_cost_lakh": ,"revised_pa_cost": "", "revised_pa_cost_lakh": ,"revised_project_cost": "","revised_project_cost_lakh": ,"revised_start_date": "","revised_start_month": ,"revised_start_year": ,"sponsoring_ministry": "","sponsoring_ministry_map": ,"start_date": "","start_month": ,"start_year": ""
  }
]
```
#### Summary json response:
```
[
  {
    "approval_date": "", "cabinet_division_map":, "cost_unit": "", "end_date": "", "end_month": "","end_year":                "","executing_agency": "","gob_cost": "","gob_cost_lakh": ,"other_cost": "","other_cost_lakh": ,"own_fund": "","own_fund_lakh": ,"pa_cost": "","pa_cost_lakh": ,"planning_division": "","project_activity": "","project_cost": "","project_cost_lakh": ,"project_id": "","project_location": [],"project_name": "","project_name_english": "","project_purpose": "","sponsoring_ministry": "","sponsoring_ministry_map": ,"start_date": "","start_month": ,"start_year": ""
  }
]
```
#### Meeting Minute json response:
```
[
  {
    "approval_date": "", "cabinet_division_map":, "cost_unit": "", "end_date": "", "end_month": "","end_year":                "","executing_agency": "","gob_cost": "","gob_cost_lakh": ,"is_ministry_project": ,"other_cost": "","other_cost_lakh": ,"own_fund": "","own_fund_lakh": ,"pa_cost": "","pa_cost_lakh": ,"planning_division": "","project_activity": "","project_benefit":"", "project_cost": "","project_cost_lakh": ,"project_id": "","project_location": [],"project_name": "","project_name_english": "","project_purpose": "","sponsoring_ministry": "","sponsoring_ministry_map": ,"start_date": "","start_month": ,"start_year": ""
  }
]

```

* ### Project Linking
Linking the current project with it's parent project.
```
Route: /data_extraction
Method: [POST]
Input: project_name

Output: [parent_project_name]
```

## Deployment

[Deploy in linux server](https://docs.google.com/document/d/1mHeeXu2POn77GdKVOf_-YjLf1zwTnsdeVglbkgBJELg/edit?usp=sharing)

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The micro-web framework used


## Authors

* **Mia Md Raihan** - *Complete work* - [website](https://mmraihan.herokuapp.com)

See also the list of [contributors](https://github.com/RaihanSabique/Data_Extraction/contributors) who participated in this project and worked in different modules.

## License

This project is licensed under the Copyright © [Department of Computer Science and Engineering, BUET](https://cse.buet.ac.bd/)

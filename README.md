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

Or easily run from directory

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
***Output JSON response is a list of dictionary and contains:***
DPP response:
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

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

[Deploy in linux server](https://docs.google.com/document/d/1mHeeXu2POn77GdKVOf_-YjLf1zwTnsdeVglbkgBJELg/edit?usp=sharing)

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

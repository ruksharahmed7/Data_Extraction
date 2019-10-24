from .costconverter import convert as costConverter
from .dateconverter import converter as dateconverter
from .dateconverter import dateconverter as approvaldateconverter
from .stmconverter import division_convert as div_convert

def convertAll(filtered_final_result):
    filtered_final_result['project_cost_lakh'] = costConverter(filtered_final_result['project_cost'],
                                                                          filtered_final_result['cost_unit'])
    filtered_final_result['gob_cost_lakh'] = costConverter(filtered_final_result['gob_cost'],
                                                                      filtered_final_result['cost_unit'])
    filtered_final_result['other_cost_lakh'] = costConverter(filtered_final_result['other_cost'],
                                                                        filtered_final_result['cost_unit'])
    filtered_final_result['own_fund_lakh'] = costConverter(filtered_final_result['own_fund'],
                                                                      filtered_final_result['cost_unit'])
    filtered_final_result['pa_cost_lakh'] = costConverter(filtered_final_result['pa_cost'],
                                                                     filtered_final_result['cost_unit'])
    filtered_final_result['revised_project_cost_lakh'] = costConverter(filtered_final_result['revised_project_cost'],
                                                                          filtered_final_result['cost_unit'])

    filtered_final_result['revised_gob_cost_lakh'] = costConverter(filtered_final_result['revised_gob_cost'],
                                                                          filtered_final_result['cost_unit'])

    filtered_final_result['revised_other_cost_lakh'] = costConverter(filtered_final_result['revised_other_cost'],
                                                                          filtered_final_result['cost_unit'])

    filtered_final_result['revised_pa_cost_lakh'] = costConverter(filtered_final_result['revised_pa_cost'],
                                                                          filtered_final_result['cost_unit'])

    start_date=filtered_final_result['start_date']
    end_date=filtered_final_result['end_date']
    print(start_date,end_date)
    filtered_final_result['start_month'],filtered_final_result['start_year']=dateconverter(filtered_final_result['start_date'])
    filtered_final_result['end_month'],filtered_final_result['end_year'] = dateconverter(filtered_final_result['end_date'])
    filtered_final_result['revised_start_month'], filtered_final_result['revised_start_year'] = dateconverter(filtered_final_result['revised_start_date'])
    filtered_final_result['revised_end_month'], filtered_final_result['revised_end_year'] = dateconverter(filtered_final_result['revised_end_date'])
    if filtered_final_result['start_month']:
        filtered_final_result['start_date']=filtered_final_result['start_month']+"'"+filtered_final_result['start_year']
    if filtered_final_result['end_month']:
        filtered_final_result['end_date'] = filtered_final_result['end_month'] + "'" + filtered_final_result['end_year']
    if filtered_final_result['revised_start_month']:
        filtered_final_result['revised_start_date'] = filtered_final_result['revised_start_month'] + "'" + filtered_final_result['revised_start_year']
    if filtered_final_result['revised_end_month']:
        filtered_final_result['revised_end_date'] = filtered_final_result['revised_end_month'] + "'" + filtered_final_result['revised_end_year']
    planning_division=filtered_final_result["planning_division"]
    print(planning_division)
    if planning_division:
        filtered_final_result['planning_division']=div_convert(planning_division)

    return filtered_final_result

def convertAll_summary(filtered_final_result):
    filtered_final_result['project_cost_lakh'] = costConverter(filtered_final_result['project_cost'],
                                                                          filtered_final_result['cost_unit'])
    filtered_final_result['start_month'],filtered_final_result['start_year']=dateconverter(filtered_final_result['start_date'])
    filtered_final_result['end_month'],filtered_final_result['end_year'] = dateconverter(filtered_final_result['end_date'])
    #for key,value in filtered_final_result.items():
    if 'gob_cost' in  filtered_final_result:
        filtered_final_result['gob_cost_lakh'] = costConverter(filtered_final_result['gob_cost'],
                                                                                   filtered_final_result['cost_unit'])
    if 'pa_cost' in filtered_final_result:
        filtered_final_result['pa_cost_lakh'] = costConverter(filtered_final_result['pa_cost'],
                                                                   filtered_final_result['cost_unit'])
    if 'own_fund' in filtered_final_result:
        filtered_final_result['own_fund_lakh'] = costConverter(filtered_final_result['own_fund'],
                                                                   filtered_final_result['cost_unit'])
    if filtered_final_result['approval_date']:
        filtered_final_result['approval_date']=approvaldateconverter(filtered_final_result['approval_date'])
    if filtered_final_result["planning_division"]:
        filtered_final_result['planning_division'] = div_convert(filtered_final_result["planning_division"])
    return filtered_final_result

def convertMM(result_dict):
    result_dict['project_cost_lakh'] = costConverter(result_dict['project_cost'],
                                                               result_dict['cost_unit'])
    result_dict['start_month'], result_dict['start_year'] = dateconverter(
        result_dict['start_date'])
    result_dict['end_month'], result_dict['end_year'] = dateconverter(
        result_dict['end_date'])
    # for key,value in filtered_final_result.items():
    if 'gob_cost' in result_dict:
        result_dict['gob_cost_lakh'] = costConverter(result_dict['gob_cost'],
                                                               result_dict['cost_unit'])
    if 'pa_cost' in result_dict:
        result_dict['pa_cost_lakh'] = costConverter(result_dict['pa_cost'],
                                                              result_dict['cost_unit'])
    if 'own_fund' in result_dict:
        result_dict['own_fund_lakh'] = costConverter(result_dict['own_fund'],
                                                               result_dict['cost_unit'])
    if result_dict["planning_division"]:
        result_dict['planning_division'] = div_convert(result_dict["planning_division"])
    if result_dict['approval_date']:
        result_dict['approval_date'] = approvaldateconverter(result_dict['approval_date'])

    return [result_dict]


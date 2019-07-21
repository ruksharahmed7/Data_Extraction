from .costconverter import convert as costConverter
from .dateconverter import converter as dateconverter

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

    filtered_final_result['start_month'],filtered_final_result['start_year']=dateconverter(filtered_final_result['start_date'])
    filtered_final_result['end_month'],filtered_final_result['end_year'] = dateconverter(filtered_final_result['end_date'])
    filtered_final_result['revised_start_month'], filtered_final_result['revised_start_year'] = dateconverter(filtered_final_result['revised_start_date'])
    filtered_final_result['revised_end_month'], filtered_final_result['revised_end_year'] = dateconverter(filtered_final_result['revised_end_date'])

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

    return filtered_final_result


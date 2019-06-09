from .costconverter import convert as costConverter
from .dateconverter import converter as dateconverter

def convertAll(filtered_final_result):
    filtered_final_result['project_cost_decimal'] = costConverter(filtered_final_result['project_cost'],
                                                                          filtered_final_result['cost_unit'])
    filtered_final_result['gob_cost_decimal'] = costConverter(filtered_final_result['gob_cost'],
                                                                      filtered_final_result['cost_unit'])
    filtered_final_result['other_cost_decimal'] = costConverter(filtered_final_result['other_cost'],
                                                                        filtered_final_result['cost_unit'])
    filtered_final_result['own_fund_decimal'] = costConverter(filtered_final_result['own_fund'],
                                                                      filtered_final_result['cost_unit'])
    filtered_final_result['pa_cost_decimal'] = costConverter(filtered_final_result['pa_cost'],
                                                                     filtered_final_result['cost_unit'])
    filtered_final_result['revised_project_cost_decimal'] = costConverter(filtered_final_result['revised_project_cost'],
                                                                          filtered_final_result['cost_unit'])

    filtered_final_result['revised_gob_cost_decimal'] = costConverter(filtered_final_result['revised_gob_cost'],
                                                                          filtered_final_result['cost_unit'])

    filtered_final_result['revised_other_cost_decimal'] = costConverter(filtered_final_result['revised_other_cost'],
                                                                          filtered_final_result['cost_unit'])

    filtered_final_result['revised_pa_cost_decimal'] = costConverter(filtered_final_result['revised_pa_cost'],
                                                                          filtered_final_result['cost_unit'])

    filtered_final_result['start_month'],filtered_final_result['start_year']=dateconverter(filtered_final_result['start_date'])
    filtered_final_result['end_month'],filtered_final_result['end_year'] = dateconverter(filtered_final_result['end_date'])

    return filtered_final_result


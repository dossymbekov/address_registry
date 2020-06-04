# address_registry

https://data.egov.kz/api/v4/s_ats/_search?size=0&apiKey=4d5fbfd8e00047d6931ede2d301c3caa&source={"aggs" : {"max_id" : { "max": { "field" : "id" }}}}

{"size":100,"query": {"terms":{"id":["2", "251448"]}}}
{"size":100,"query": {"aggs" : {"max_price" : { "max" : { "field" : "id" } }}}}
source={"aggs" : {"max_id" : { "terms" : { "field" : "name_kaz" } }}}

{"aggs" : {"max_price" : { "max" : { "field" : "id" } }}}
https://data.egov.kz/api/v4/s_ats/_search?size=0&apiKey=4d5fbfd8e00047d6931ede2d301c3caa&source={"aggs" : {"max_id" : { "terms": { "field" : "d_ats_type_id" }}}}
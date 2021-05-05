# VietnamAPI
An API to provide information about Vietnam

/api/vietnam/province.js - pulls the provinces and their province_id
/api/vietnam/districts/{province_id} - pulls the districts in the provinces, their ids, their congress_id, and future information about the district
/api/QuocHoi/QuocHoiXV/{congress_id} - pulls unit name, unit's district (id or string?), candidates_id
/api/QuocHoi/QuocHoiXV/candidates/{candidates_id} - pulls information about candidates

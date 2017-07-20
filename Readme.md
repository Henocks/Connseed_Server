# Just Server Not More

<a href = "169.56.126.151"> LINK </a>


# API LIST

POST: /data/postrawdata

### Parameter    
    
    device : device pk (id)
    wtr    : Wtr Value
    ppm    : PPM Value
    tmp    : Temperature Value
    hum    : Humidity Value
    lux    : Lux Value


GET: /data/getalldata

### Parameter
    device : device pk(id)


GET: /data/getcurrentdata

### Parameter
    device : device pk(id)


GET: /data/getdatedata

### Parameter
    device : device pk(id)
    date   : %Y-%m-%d

#### Example
    /data/getdatedata?device=1&date=2017-07-19

GET: /data/devicelist

    
### Require Login (USER) Information.

#### Response
    application/json; charset=utf-8
    'id', 'EUI','Battery', 'Nickname'



POST: /login

### Parameter
    id : account id
    pw : password

#### Response 
    OK                  : status 200
    Invalid  GET Method : status 401
    IsLogined           : status 401
    Parameter Denied    : status 401
    Login InValid       : status 401
    anyexception        : status 400


GET: /data/getstatisticaldata_day

### Parameter
    device : device pk(id)
    date   : %Y-%m-%d


GET: /data/getstatisticaldata_week

### Parameter
    device : device pk(id)
    date   : %Y-%m-%d


GET: /data/getstatisticaldata_month

### Parameter
    device : device pk(id)
    date   : %Y-%m-%d



#### Response 
    OK                  : status 200
    Invalid  GET Method : status 401
    IsLogined           : status 401
    Parameter Denied    : status 401
    Login InValid       : status 401
    anyexception        : status 400




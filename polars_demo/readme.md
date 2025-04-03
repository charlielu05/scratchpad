### data dictionary
https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf

### number of files
find nyc_cab_data -type f | wc -l

### file size
du -sh nyc_cab_data/

### OLS 
X = X-X.mean()
Y = Y-Y.mean()
w = inv(X.T.dot(X)) * X.T.dot(Y)
w = X*Y / (X^2)
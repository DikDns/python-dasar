# Casting Tipe Data
# CARA MENGONVERSI TIPE DATA
# mengubah ke int   |   int( [data_awal] )
# mengubah ke float |   float( [data_awal] )
# mengubah ke bool  |   bool( [data_awal] )
# mengubah ke str   |   str( [data_awal] )

data = 1

print("Data         : ", data)
print(" | Tipe : ", type(data))

dataToFloat = float( data )

print("dataToFloat  : ", dataToFloat)
print(" | Tipe : ", type(dataToFloat))

dataToBool = bool( data )

print("dataToBool  : ", dataToBool)
print(" | Tipe : ", type(dataToBool))

dataToStr = str( data )

print("dataToStr  : ", dataToStr)
print(" | Tipe : ", type(dataToStr))
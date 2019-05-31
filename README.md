# freecad_point_cloud_visualizer

## Kullanım
- python3 visualizer_maker.py

### Veritabanından nokta bulutunu çekme
- Pyodbc içerisindeki connect.py veri tabanındaki nokta bulutunu mech.db'ye yazar.
- Visualizer programı çalıştırılarak, freecad fonksiyon dosyası oluşturulur.

### Freecad açılarak:
- with open('db.point', 'r') as code_line:
- &emsp;content = code_line.read()
- exec(content)

Nokta bulutunun görselleştirme işlemine başlanılacaktır.



- Creator : @ Burak Büyükyüksel
- Version : 0.1

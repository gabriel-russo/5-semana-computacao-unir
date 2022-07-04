# Python: Exemplo de processamento de raster com GDAL

As imagens foram retiradas do satélite CBERS4A do sensor WPM.

---

Bibliotecas Necessárias para utilizar o script:
- GDAL

<img height="150" src="../assets/img/python_gdal.png" width="150"/>

---
Detalhes do raster utilizado nesse exemplo:

- ID: CBERS4A_WPM_22912420210730
- Nome da coleção: CBERS4A_WPM_L4_DN
- Data: 30/07/2021
- Hora: 14:58:34
- Quantidade de nuvem: 0%
- Possui as Bandas: pan, vermelha, verde, azul, nir
- Órbida: 229
- Ponto: 124
- Satélite: CBERS4A
- Sensor: WPM

Obs1: Bandas vermelha, verde e azul possuem a resolução de 8 metros

Obs2: Banda panchromática possui a resolução de 2 metros

---

## Visualizando a extensão do raster:
![](../assets/img/python_imagem_bruta.png)

## Área escolhida para o recorte
![](../assets/img/python_unir_area_interesse_recorte.png)

## Imagens recortadas

### Banda Vermelha (B3)
![](../assets/img/python_unir_b3.png)

### Banda Verde (B2)
![](../assets/img/python_unir_b2.png)

### Banda Azul (B1)
![](../assets/img/python_unir_b1.png)

## Resultados do processamento

### Composição TRUE COLOR (B3, B2, B1) (Merge)
![](../assets/img/python_unir_truecolor.png)

### Fusão da imagem TRUE COLOR com a banda Pan (Pansharpening)
![](../assets/img/python_unir_pansharp.png)

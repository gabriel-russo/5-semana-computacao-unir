from osgeo.gdal import Warp, WarpOptions
from osgeo_utils import gdal_merge, gdal_pansharpen
from os.path import splitext, join
from os import getcwd, cpu_count
from glob import glob

# ###########################################################
# Fazer o recorte da área de interesse utilizando GDAL Warp #
# ###########################################################

caminho_absoluto = getcwd()
area_de_interesse = r'Recorte UNIR/recorte_unir.shp'

# Configurando as opções de corte da imagem
opcoes = WarpOptions(cutlineDSName=area_de_interesse,  # Nome do Dataset que ira servir de corte
                     cropToCutline=True)  # Fazer o corte utilizando as extenções máximas do Dataset (cutlineDSName)

# Fazer um recorte para cada raster
for raster in glob('*.tif'):
    nome_arquivo, extensao = splitext(raster)

    caminho_arquivo = join(caminho_absoluto, raster)

    caminho_arquivo_corte = join(caminho_absoluto, nome_arquivo + '_recortado.tif')
    Warp(srcDSOrSrcDSTab=caminho_arquivo,
         destNameOrDestDS=caminho_arquivo_corte,
         options=opcoes)

# #############################################################################
# Criando a composição True color (B3, B2, B1) utilizando GDAL Merge #
# #############################################################################

pancromatica = vermelho = verde = azul = ''

# Para cada imagem recortada, irei separar por banda
for arquivo in glob('*_recortado.tif'):
    if 'BAND3' in arquivo:
        vermelho = join(caminho_absoluto, arquivo)
    if 'BAND2' in arquivo:
        verde = join(caminho_absoluto, arquivo)
    if 'BAND1' in arquivo:
        azul = join(caminho_absoluto, arquivo)
    if 'BAND0' in arquivo:
        pancromatica = join(caminho_absoluto, arquivo)

output_raster_colorido = join(caminho_absoluto, r'Raster_colorido.tif')

gdal_merge.main(['', '-o', output_raster_colorido] +
                [vermelho, verde, azul] +
                ['-co', 'COMPRESS=NONE', '-ot', 'Int16', '-separate'])

# ########################################################################################
# Aumentando a resolução da imagem com a fusão da banda pancromática (B0) e a true color #
# ########################################################################################

output_pansharp = join(caminho_absoluto, r'Raster_pansharp.tif')

gdal_pansharpen.gdal_pansharpen(pan_name=pancromatica,
                                spectral_names=[output_raster_colorido],
                                band_nums=[1, 2, 3],
                                num_threads=cpu_count(),
                                dst_filename=output_pansharp)

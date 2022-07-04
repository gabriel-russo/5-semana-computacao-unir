-- Criando um índice espacial para melhor desempenho das operações
CREATE INDEX index_biomas ON public."BRA_BIOMAS" USING GIST (geom);
CREATE INDEX index_queimadas ON public.queimadas_03_04_julho USING GIST (geom);

-- Executando uma consulta espacial

-- INTERSECÇÃO
-- Se uma geometria compartilha um espaço em comum com outra, então eles se interseccionam.

-- QUANTIDADE DE DETECÇÕES DE FOCOS DE CALOR NO DIA 03 E 04 DE JULHO EM CADA BIOMA:
SELECT biomas."NOME" AS bioma, count(queimadas.id) AS deteccoes FROM public."BRA_BIOMAS" AS biomas
JOIN public.queimadas_03_04_julho AS queimadas ON ST_INTERSECTS(biomas.geom, queimadas.geom)
GROUP BY biomas."NOME";

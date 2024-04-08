select count(*) as COUNT
from ECOLI_DATA 
where GENOTYPE & 5 and not (GENOTYPE & 2)

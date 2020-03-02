let rec gamma n p = 
  if n = 0 then p + 1 else
  if n = 1 then p*p + p +1 else
    somme_gamma n p 0 0
and somme_gamma n p i som = 
    if i < n then
      somme_gamma n p (i+1) (som + ((gamma i p)*(gamma (n-1-i) (p+i))))
    else som

;;

let g = gamma 20 0 in  print_int g;;
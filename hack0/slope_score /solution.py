def slope_style_score(scores):
 scores.remove(min(scores))
 scores.remove(max(scores))
 final = sum(scores) / len(scores) 
 print ('%.2f' %(final))
 return ('%.2f' %(final))
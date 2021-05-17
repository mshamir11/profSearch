interest = ["Artificial intelligence","Computer vision","Machine learning","data mining","Natural language processing",	"Web","information retrieval", 
            "Computer architecture","Computer networks","Computer security","Databases","Design automation","Embedded","High-performance computing","Operating systems",
            "Programming languages","Software engineering","Algorithms","Cryptography","Logic & verification","deep learning", '3D Computer Vision',
 'Earth and Planetary Sciences', 'gesture input', 'interactive visualization', 'imagens médicas', 'Cognitive vision', 'Developing Regions',
 'Answer Sets', 'Computer-Aided Diagnosis', 'Fluid mechanics', 'AI systems', 'Algorithmic Differentiation', 'Social Artificial Intelligence',
 'Engineering of Interactive Systems', 'Automated Network Protocol Testing', 'Antibody Engineering',
 'Data Intensive Computing', 'Geometric Computing', 'turbulence', 'spatial cognition', 'Information Theoretic Security',
 'Virutal and Augmented Reality', 'Service Science', 'Topic Modelling', 'Earth and Planetary Sciences',
 'gesture input', 'interactive visualization', 'imagens médicas', 'Cognitive vision']
from scipy import spatial
from sent2vec.vectorizer import Vectorizer

final_dic={}
i = 0
for item1 in interest:

  dist_list=[]
  for item2 in interest:
    if item1!=item2:
      query=[item1,item2]
      vectorizer=Vectorizer()
      vectorizer.bert(query)
      vectors_bert = vectorizer.vectors

      dist = spatial.distance.cosine(vectors_bert[0], vectors_bert[1])
      dist_list.append((item2,dist))

  dist_list.sort(key=lambda x:x[1])
  required = dist_list[:5]
  final_dic[item1]=required
  i+=1
  print(i)
  #break

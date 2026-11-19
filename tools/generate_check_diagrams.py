#!/usr/bin/env python3
"""Create 36 unique bilingual problem/fix SVG diagrams for the UE5 Tools docs.

The drawings are purpose-built vector explanations, NOT screenshots and not
claims about a particular scanned asset. No Blender dependency required.
"""
from pathlib import Path
from html import escape
import json, math, textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/assets/diagrams'
CONTENT = ROOT / 'content'
BG='#0b1019'; PANEL='#121e2b'; PANEL2='#172738'; WHITE='#edf5fa'; DIM='#a5b6c5'
RED='#fa786d'; RED_BG='#4d252b'; GREEN='#64d8b3'; GREEN_BG='#164235'
BLUE='#6fb6df'; LINE='#476278'; AMBER='#fac878'; SILVER='#d7e0e9'

LABELS={
 'empty_mesh':(('Пустая модель','Объект с геометрией','В объекте нет граней и вершин.','В модели есть геометрия.'),('Empty mesh','Mesh with geometry','Object has no mesh elements.','Mesh contains actual geometry.')),
 'ngons':(('Одна грань с 6 углами','Контролируемая сетка','Большой N-gon может непредсказуемо разбиться.','Разбиение сетки контролируется.'),('One face with six corners','Controlled topology','One N-gon may triangulate unpredictably.','The intended triangulation is explicit.')),
 'nonmanifold':(('Три грани на ребре','Две грани на ребре','Одно ребро принадлежит трём граням.','Обычное внутреннее ребро имеет две грани.'),('Three faces share an edge','Two faces share an edge','A single edge is shared by three faces.','A regular inner edge has two faces.')),
 'degenerate':(('Грань почти без площади','Обычный треугольник','Вершины почти совпадают — площадь ≈ 0.','У треугольника нормальная площадь.'),('Almost zero-area triangle','Healthy triangle','Vertices are nearly collinear: area ≈ 0.','The triangle has a usable area.')),
 'zero_edges':(('Ребро длиной 0','Ребро нормальной длины','Начальная и конечная вершины совпадают.','Между вершинами есть расстояние.'),('Zero-length edge','Healthy edge','Its two endpoints occupy one position.','The endpoints are separated.')),
 'duplicate_faces':(('Две грани на одном месте','Оставлена одна грань','Совпадающие грани вызывают наложение.','Лишняя копия удалена.'),('Two faces in one location','Only one face remains','Coincident polygons can cause Z-fighting.','The redundant copy is removed.')),
 'loose_edges':(('Лишние рёбра','Чистая сетка','Отдельные рёбра не входят ни в одну грань.','Лишние рёбра удалены.'),('Loose edges','Clean topology','Detached edges are not used by any face.','Unneeded detached edges removed.')),
 'loose_verts':(('Отдельные вершины','Чистая сетка','Точки не связаны с рёбрами или гранями.','Лишние точки удалены.'),('Loose vertices','Clean topology','These points are not part of a face or edge.','Unused points are removed.')),
 'boundary':(('Открытый край','Замкнутая поверхность','Красным выделено ребро только с одной гранью.','Отверстие закрыто, если это требуется.'),('Open boundary','Closed surface','Red edges belong to just one polygon.','The hole is closed if required.')),
 'nearverts':(('Почти совпавшие точки','Одна точка соединения','Очень близкие вершины могут быть дублями.','Проверенные дубликаты объединены.'),('Almost coincident vertices','Single joined vertex','Very close points may be accidental doubles.','Verified duplicates are merged.')),
 'scale':(('Scale не применён','Scale = 1, 1, 1','Геометрия растянута масштабом объекта.','Ctrl+A → Scale; форма остаётся той же.'),('Unapplied object scale','Scale = 1, 1, 1','Object dimensions depend on object Scale.','Ctrl+A → Scale keeps the visible shape.')),
 'rotation':(('Rotation не применён','Rotation = 0°, 0°, 0°','Объект повернут на уровне Transform.','Ctrl+A → Rotation без смены внешнего вида.'),('Unapplied rotation','Rotation = 0°, 0°, 0°','The rotation exists on object Transform.','Ctrl+A → Rotation preserves appearance.')),
 'mirrored':(('Отрицательный Scale','Положительный Scale','Зеркальный масштаб меняет ориентацию осей.','Проверь зеркальность перед экспортом.'),('Negative scale','Positive object scale','Mirror scaling changes coordinate handedness.','Review the mirror before export.')),
 'zero_scale':(('Scale Y = 0','Scale Y = 1','Одна ось геометрии схлопнута.','Верни ненулевой масштаб оси.'),('Scale Y = 0','Scale Y = 1','One object axis is fully collapsed.','Restore a nonzero axis scale.')),
 'winding':(('Одинаковый обход ребра','Противоположный обход','Обе грани обходят общее ребро одинаково.','Соседние грани согласованы.'),('Same edge direction','Opposite edge directions','Two faces traverse a shared edge alike.','Adjacent faces traverse it oppositely.')),
 'inverted_normals':(('Нормали смотрят внутрь','Нормали смотрят наружу','У замкнутой оболочки все нормали внутрь.','Нормали оболочки наружу.'),('Inward-facing normals','Outward-facing normals','A closed shell has inward normals.','Normals point out of the shell.')),
 'steep_smooth':(('Сглажен резкий угол','Граница сглаживания','Smooth через острый угол портит шейдинг.','Раздели нормали на резком ребре.'),('Smoothed hard corner','Sharp normal boundary','Smooth shading spans a hard crease.','Mark a sharp edge where needed.')),
 'no_uv':(('UV-карты нет','UV-карта создана','В UV Editor нечего редактировать.','Модель получила развёртку.'),('No UV map','UV map created','The UV Editor has no mapped islands.','The mesh now has an unwrap.')),
 'collapsed_uv':(('UV-грань схлопнута','UV-грань имеет площадь','Три UV-точки лежат на одной линии.','UV-остров больше не вырожден.'),('Collapsed UV face','Valid UV area','UV corners collapse onto a single line.','The polygon has actual UV area.')),
 'outside_uv':(('UV за пределами 0–1','UV внутри 0–1','Для одноплиточной UV это проблема.','Остров внутри нужной плитки.'),('UV outside 0–1','UV inside 0–1','An issue for single-tile UV workflows.','The island stays inside the target tile.')),
 'uv_overlap':(('UV-острова наложены','UV-острова разделены','Части текстуры используют одну область UV.','Острова разнесены без пересечений.'),('Overlapping UV islands','Separated UV islands','Different surfaces share UV texture space.','Islands no longer overlap.')),
 'uv_stretch':(('Искажённый checker','Ровный checker','Клетки растянуты — текстура исказится.','Пропорции checker сохраняются.'),('Stretched checker','Even checker','Rectangular cells reveal texture distortion.','Square cells retain proportions.')),
 'no_material':(('Материал не назначен','Материал назначен','Материал для объекта не задан.','На объект назначен материал.'),('No assigned material','Material assigned','The object has no assigned material.','A material slot is assigned.')),
 'empty_slot':(('Пустой слот','Нет пустого слота','Material slot существует без материала.','Слот заполнен или удалён.'),('Empty material slot','No empty slot','An existing material slot has no material.','The slot is assigned or removed.')),
 'unassigned_faces':(('Неверный индекс материала','Корректный индекс','Грань ссылается на отсутствующий слот.','Индекс грани указывает на существующий слот.'),('Invalid face material index','Valid material index','A polygon refers to an absent slot.','The face refers to an existing slot.')),
 'unused_materials':(('Лишний слот материала','Только нужные слоты','Один материал не используется гранями.','Ненужный слот убран.'),('Unused material slot','Only used slots remain','No face uses one of the material slots.','An unused slot has been removed.')),
 'missing_image':(('Image Texture: Empty','Image Texture: Assigned','У Image Texture отсутствует изображение.','К узлу назначено изображение.'),('Image Texture: Empty','Image Texture: Assigned','An Image Texture node has no image.','An image is assigned to the node.')),
 'missing_texture':(('Файл не найден','Файл найден','Ссылка на внешний файл разорвана.','Файл доступен по указанному пути.'),('Texture file missing','Texture file found','The external image path is broken.','The image resolves to an existing file.')),
 'big_texture':(('Чрезмерное разрешение','Разумное разрешение','8192² может быть слишком много для пропса.','Подбери размер по качеству и бюджету.'),('Excessive texture size','Right-sized texture','8192² may be unnecessary for a prop.','Choose resolution for the target asset.')),
 'poly_budget':(('Выше лимита','В пределах лимита','Пример: 65k треугольников при лимите 20k.','Пример: после упрощения 16k.'),('Above polygon budget','Within polygon budget','Example: 65k triangles against a 20k target.','Example after reduction: 16k triangles.')),
 'texel_deviation':(('Неравномерная плотность','Равномерная плотность','Размер клеток на деталях сильно разный.','Детали имеют сравнимую плотность.'),('Uneven texel density','Consistent texel density','Checker size differs between mesh parts.','Both pieces have a similar texel scale.')),
 'texel_target':(('Ниже цели','Около цели','Пример: 256 px/м против цели 512 px/м.','Пример: 512 px/м соответствует цели.'),('Below target','Near target','Example: 256 px/m vs a 512 px/m target.','Example: 512 px/m matches the target.')),
 'pivot':(('Origin далеко от модели','Origin в нужном месте','Поворот и установка могут быть неудобными.','Origin перенесён в рабочую точку.'),('Origin outside object','Origin in useful location','Placement and rotation become awkward.','Origin is placed at the intended point.')),
 'lightmap_missing':(('Нет Lightmap UV','Есть Lightmap UV','Вторая UV-карта не подготовлена.','Добавлена отдельная UV-карта для lightmap.'),('No lightmap UV','Dedicated lightmap UV','A lightmap channel has not been prepared.','A separate lightmap UV channel exists.')),
 'lightmap_bounds':(('Lightmap за пределами 0–1','В пределах 0–1','Lightmap UV выходит за границы тайла.','Все острова внутри единичной плитки.'),('Lightmap outside 0–1','Inside the 0–1 tile','A lightmap island spills outside its tile.','All islands stay inside the unit square.')),
 'lightmap_overlap':(('Перекрытие lightmap UV','Неперекрывающиеся UV','Наложение мешает запеканию освещения.','Острова разделены с отступами.'),('Lightmap UV overlap','Unique packed lightmap UVs','Overlaps break baked lighting.','Separate islands include safe padding.')),
}

class Drawing:
 def __init__(self): self.a=[]
 def add(self,s): self.a.append(s)
 def rect(self,x,y,w,h,fill='none',stroke='none',sw=1,r=0,opacity=None):
  self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"'+(f' opacity="{opacity}"' if opacity else '')+'/>')
 def poly(self,pts,fill='none',stroke=BLUE,sw=2,opacity=None):
  self.add(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"'+(f' opacity="{opacity}"' if opacity else '')+'/>')
 def line(self,x,y,xx,yy,color=BLUE,sw=3,dash=None):
  self.add(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
 def path(self,d,color=BLUE,sw=3,fill='none',dash=None):
  self.add(f'<path d="{d}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" fill="{fill}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
 def text(self,x,y,s,color=WHITE,size=18,weight=500,anchor='start'):
  self.add(f'<text x="{x}" y="{y}" fill="{color}" font-family="DejaVu Sans, Arial, sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(str(s))}</text>')
 def circle(self,cx,cy,r,fill='none',stroke=BLUE,sw=2):
  self.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
 def arrow(self,x,y,xx,yy,color=RED,sw=3):
  self.line(x,y,xx,yy,color,sw)
  ang=math.atan2(yy-y,xx-x)
  for side in [-1,1]:
   a=ang+math.pi+side*0.55
   self.line(xx,yy,xx+11*math.cos(a), yy+11*math.sin(a),color,sw)
 def x(self,x,y,color=RED,r=10):
  self.line(x-r,y-r,x+r,y+r,color,3);self.line(x-r,y+r,x+r,y-r,color,3)
 def tick(self,x,y): self.path(f'M {x-12} {y} l 8 9 l 19 -22',GREEN,4)
 def mesh_cube(self,x=150,y=53,w=130,h=107,dep=33,top=True,face=True,red=False,wire=True):
  # Proper projected front/top/side surfaces, so the object has recognizable volume.
  sc=RED if red else BLUE
  self.poly([(x,y),(x+dep,y-dep*.55),(x+w+dep,y-dep*.55),(x+w,y)],'#24384a',sc,2)
  self.poly([(x+w,y),(x+w+dep,y-dep*.55),(x+w+dep,y+h-dep*.55),(x+w,y+h)],'#1a3142',sc,2)
  self.poly([(x,y),(x+w,y),(x+w,y+h),(x,y+h)],'#284355',sc,2)
  if wire:
   self.line(x+w/2,y,x+w/2,y+h,LINE,1)
   self.line(x,y+h/2,x+w,y+h/2,LINE,1)
  return x,y,w,h,dep
 def grid(self,x=92,y=35,w=235,h=166,alpha=0.45):
  self.rect(x,y,w,h,'#122737',LINE,1,6)
  for i in range(1,5):
   xx=x+w*i/5;yy=y+h*i/5
   self.line(xx,y,xx,y+h,LINE,0.65)
   self.line(x,yy,x+w,yy,LINE,0.65)
  self.text(x+10,y-10,'0',DIM,13)
  self.text(x+w-7,y+h+17,'1',DIM,13,'end')
 def uv_poly(self,pts,bad=False):
  self.poly(pts,'#7b3840' if bad else '#1d7266',RED if bad else GREEN,3)
  for x,y in pts:self.circle(x,y,3,WHITE,'none',0)
 def checker(self,x,y,w,h,nx,ny,color=BLUE):
  self.rect(x,y,w,h,'#132b3a',LINE,1,5)
  for row in range(ny):
   for col in range(nx):
    if (row+col)%2==0:
     self.rect(x+col*w/nx+1,y+row*h/ny+1,w/nx-2,h/ny-2,'#58839a','none',0,0,0.38)
  self.rect(x,y,w,h,'none',color,2,4)
 def field(self,x,y,name,value,color=WHITE,w=275):
  self.rect(x,y,w,33,'#0d1722',LINE,1,6)
  self.text(x+13,y+22,name,DIM,15)
  self.text(x+w-12,y+22,value,color,15,700,'end')
 def slots(self,entries):
  self.rect(90,17,260,188,'#0e1722',LINE,1,8)
  self.text(106,39,'MATERIAL SLOTS',DIM,14,700)
  for i,(nm,flag) in enumerate(entries):
   y=52+i*42
   self.rect(106,y,226,34,'#172c3d',RED if flag else GREEN,1.5,5)
   self.circle(124,y+17,7,RED if flag else GREEN,'none',0)
   self.text(143,y+22,nm,WHITE if not flag else RED,15,500)
 def node(self,filename,issue):
  self.rect(102,33,241,155,'#203040',LINE,2,8)
  self.rect(102,33,241,30,'#35435e','none',1,8)
  self.text(114,54,'Image Texture',WHITE,15,700)
  self.rect(125,83,194,55,'#111b29',LINE,1,6)
  if issue:self.text(220,116,filename,RED,18,600,'middle')
  else:self.text(220,116,filename,GREEN,17,600,'middle')
  self.circle(337,150,6,GREEN,'none',0)
 def axis_cross(self,x,y,color=AMBER):
  self.line(x-19,y,x+19,y,color,2.5)
  self.line(x,y-19,x,y+19,color,2.5)
  self.circle(x,y,5,BG,color,2)
 def graph(self,vertices,color=BLUE,wire=True):
  self.poly(vertices,'#264b60',color,2.5)
  if wire:
   for x,y in vertices:self.circle(x,y,4,WHITE,'none',0)

# One dedicated visual scene per check, with bad/fixed state.
def scene(key,d,good=False):
 color=GREEN if good else RED
 if key=='empty_mesh':
  if good:d.mesh_cube(152,61,128,96)
  else:
   d.path('M 115 137 L 326 137',LINE,2,dash='6 8');d.path('M 218 35 L 218 203',LINE,2,dash='6 8');d.x(220,116)
 elif key=='ngons':
  pts=[(145,60),(246,42),(317,96),(295,180),(202,193),(120,150)]
  d.graph(pts,color)
  if good:
   for i in range(2,len(pts)-1):d.line(*pts[0],*pts[i],GREEN,2)
 elif key=='nonmanifold':
  d.line(202,44,202,191,color,5)
  d.poly([(202,44),(122,89),(202,191)],'#294e63',BLUE,2)
  d.poly([(202,44),(288,99),(202,191)],'#294e63',BLUE,2)
  if not good:
   d.poly([(202,44),(202,191),(330,139)],'#71353c',RED,3)
  d.circle(202,119,8,color,'none',0)
 elif key=='degenerate':
  pts=[(137,176),(305,179),(220,181)] if not good else [(137,185),(305,177),(222,48)]
  d.graph(pts,color)
  if not good:d.x(223,180)
 elif key=='zero_edges':
  d.line(110,133,224,133,BLUE,4)
  d.circle(110,133,6,WHITE,'none',0)
  ex=224 if not good else 321
  d.circle(ex,133,7,color,'none',0)
  d.arrow(255,102,224 if not good else 321,128,color)
  if good:d.line(224,133,321,133,GREEN,4)
 elif key=='duplicate_faces':
  # Two identical quads, shown slightly exploded on the left to make coincidence understandable.
  pts=[(119,166),(223,91),(326,150),(217,215)]
  d.graph(pts,GREEN if good else RED)
  if not good:
   d.poly([(x+15,y-14) for x,y in pts],'#873e46',RED,3,opacity='.76')
   d.line(239,96,270,65,RED,2,dash='5 6');d.text(290,71,'×2',RED,22,700)
 else:
  if key=='loose_edges':
   d.mesh_cube(115,68,112,105)
   if not good:
    d.line(300,73,349,112,RED,5);d.line(309,158,358,190,RED,5)
    for xy in [(300,73),(349,112),(309,158),(358,190)]:d.circle(*xy,5,RED,'none',0)
  elif key=='loose_verts':
   d.mesh_cube(105,68,112,105)
   if not good:
    for x,y in [(296,76),(348,111),(325,181)]:d.circle(x,y,6,RED,'none',0)
  elif key=='boundary':
   x,y,w,h,dep=144,74,134,105,33
   d.mesh_cube(x,y,w,h,dep)
   if not good:
    d.poly([(x,y),(x+dep,y-dep*.55),(x+w+dep,y-dep*.55),(x+w,y)],'#0b1019',RED,5)
    d.arrow(345,51,292,69,RED)
  elif key=='nearverts':
   d.graph([(135,176),(214,45),(330,181)],BLUE)
   d.circle(214,45,7,GREEN if good else RED,'none',0)
   if not good:
    d.circle(227,53,6,RED,'none',0);d.line(214,45,227,53,RED,3,dash='3 4')
  elif key in ('scale','rotation','mirrored','zero_scale'):
   if key=='zero_scale':
    if good:d.mesh_cube(146,58,130,113)
    else:
     d.poly([(119,94),(341,94),(341,104),(119,104)],'#803f40',RED,3)
     d.line(119,118,341,118,RED,2,dash='6 7')
    d.field(96,174,'Scale Y','1.000' if good else '0.000',GREEN if good else RED)
   else:
    d.mesh_cube(150,47,122,93)
    if key=='scale':d.field(95,166,'Scale X','1.000' if good else '2.400',GREEN if good else RED)
    elif key=='rotation':
     if not good:d.path('M 90 112 A 95 95 0 0 1 193 28',AMBER,3)
     d.field(95,166,'Rotation Z','0°' if good else '45°',GREEN if good else RED)
    elif key=='mirrored':
     if not good:d.arrow(350,89,297,89,RED)
     d.field(95,166,'Scale X','1.000' if good else '-1.000',GREEN if good else RED)
  elif key=='winding':
   d.poly([(105,58),(221,58),(221,180),(105,180)],'#29495d',BLUE,2.5)
   d.poly([(221,58),(336,58),(336,180),(221,180)],'#29495d',BLUE,2.5)
   d.line(221,58,221,180,color,4)
   d.arrow(210,70,210,161,color)
   d.arrow(233,70 if not good else 161,233,161 if not good else 70,color)
  elif key=='inverted_normals':
   d.circle(220,113,80,'#223d4d',BLUE,2)
   for angle in range(0,360,45):
    a=math.radians(angle)
    r0=78 if not good else 53; r1=39 if not good else 99
    d.arrow(220+r0*math.cos(a),113+r0*math.sin(a),220+r1*math.cos(a),113+r1*math.sin(a),color,2.8)
  elif key=='steep_smooth':
   d.poly([(110,165),(215,51),(312,165)],'#234557',BLUE,2)
   d.poly([(215,51),(320,67),(312,165)],'#2b5067',BLUE,2)
   d.line(215,51,312,165,color,5)
   if good:
    d.arrow(204,90,177,63,GREEN);d.arrow(257,91,301,66,GREEN)
   else:
    d.arrow(240,105,239,48,RED);d.path('M 165 110 Q 222 70 280 110',AMBER,3,dash='5 6')
  elif key in ('no_uv','collapsed_uv','outside_uv','uv_overlap','uv_stretch','lightmap_bounds','lightmap_overlap','lightmap_missing'):
   if key=='no_uv':
    if good:
     d.grid(105,34,232,171)
     d.uv_poly([(131,66),(230,61),(218,152),(138,164)])
    else:
     d.grid(105,34,232,171);d.text(222,123,'NO UV',RED,23,700,'middle')
   elif key=='collapsed_uv':
    d.grid(105,34,232,171)
    if good:d.uv_poly([(148,178),(280,162),(221,60)])
    else:
     d.line(142,125,301,125,RED,5);d.circle(142,125,5,RED,'none',0);d.circle(301,125,5,RED,'none',0);d.circle(225,125,6,RED,'none',0)
   elif key in ('outside_uv','lightmap_bounds'):
    d.grid(105,34,232,171)
    if good:d.uv_poly([(139,80),(234,68),(286,130),(186,169)])
    else:d.uv_poly([(282,63),(382,47),(409,129),(309,167)],bad=True)
   elif key in ('uv_overlap','lightmap_overlap'):
    d.grid(105,34,232,171)
    d.uv_poly([(129,71),(233,61),(237,131),(143,145)],bad=False)
    if good:d.uv_poly([(244,142),(303,136),(319,188),(250,190)],bad=False)
    else:d.uv_poly([(167,83),(283,76),(291,150),(184,166)],bad=True)
    if key=='lightmap_overlap' and good:
     d.arrow(234,159,251,158,GREEN,2)
   elif key=='uv_stretch':
    d.checker(118,39,223 if not good else 165,169,10 if not good else 5,5,color)
    if not good:d.arrow(163,225,291,225,RED)
    else:d.tick(352,150)
   elif key=='lightmap_missing':
    d.rect(99,38,261,151,'#0c1521',LINE,2,9)
    d.text(117,68,'UV MAPS',DIM,15,700)
    d.field(114,83,'0','UVMap',GREEN,227)
    d.field(114,133,'1','Lightmap' if good else '— Missing —',GREEN if good else RED,227)
  elif key in ('no_material','empty_slot','unassigned_faces','unused_materials'):
   if key=='no_material': d.slots([('Stone' if good else '— No material —',not good)])
   elif key=='empty_slot': d.slots([('Stone',False),('Metal' if good else '— Empty —',not good)])
   elif key=='unassigned_faces':
    d.slots([('Stone',False),('Wood',False)])
    d.field(106,153,'Face material index','1' if good else '5',GREEN if good else RED,226)
   else:d.slots([('Stone',False),('Metal',False)]+([] if good else [('Unused_Mat',True)]))
  elif key in ('missing_image','missing_texture','big_texture'):
   if key=='missing_image':d.node('wood.png' if good else 'None',not good)
   elif key=='missing_texture':
    d.node('wood.png' if good else 'Missing file',not good)
    d.field(104,187,'Path','//wood.png' if good else '//old/wood.png',GREEN if good else RED,244)
   else:
    d.rect(124,29,202,161,'#243d50',color,2,5)
    for i in range(8):
     d.line(124+(i+1)*202/9,29,124+(i+1)*202/9,190,LINE,1)
     d.line(124,29+(i+1)*161/9,326,29+(i+1)*161/9,LINE,1)
    d.text(225,115,'2048²' if good else '8192²',color,27,700,'middle')
  elif key=='poly_budget':
   d.text(97,62,'TRIANGLES',DIM,17,700)
   d.rect(97,89,280,18,'#142434',LINE,1,10)
   d.rect(97,89,210 if good else 270,18,GREEN if good else RED,'none',0,9)
   d.line(315,72,315,120,AMBER,2,dash='5 4')
   d.text(315,139,'20k target',AMBER,14,600,'middle')
   d.text(224,184,'16k' if good else '65k',color,30,700,'middle')
  elif key=='texel_deviation':
   d.checker(88,46,133,143,7,7,GREEN)
   d.checker(240,46,133,143,7 if good else 3,7 if good else 3,color)
   if not good:d.arrow(223,117,238,117,RED,2)
  elif key=='texel_target':
   d.text(101,60,'TARGET: 512 px/m',DIM,17,700)
   d.rect(101,87,275,25,'#172838',LINE,1,7)
   d.rect(101,87,215 if good else 96,25,color,'none',0,6)
   d.line(316,75,316,125,AMBER,3,dash='4 4')
   d.text(238,184,'512 px/m' if good else '256 px/m',color,28,700,'middle')
  elif key=='pivot':
   d.mesh_cube(147,47,135,115)
   d.axis_cross(215 if good else 90,169 if good else 201,GREEN if good else RED)
   if not good:d.path('M 110 196 Q 140 218 181 174',RED,2,dash='5 5')
  else:raise KeyError(key)


def caption_lines(s, max_chars=39):
 return textwrap.wrap(s,width=max_chars,break_long_words=False,break_on_hyphens=False)[:2]


def render(key,lang,info):
 label_bad,label_ok,desc_bad,desc_good=info
 d=Drawing()
 d.rect(0,0,1000,440,BG)
 d.rect(18,18,964,404,PANEL,LINE,1,16)
 d.text(43,53, key.replace('_',' ').upper(),WHITE,20,700)
 d.text(954,51,'UE5 TOOLS · PRE-EXPORT CHECK',DIM,13,600,'end')
 for idx,isgood in enumerate((False,True)):
  ox=30 if idx==0 else 510
  d.rect(ox,76,460,328,'#12202f',LINE,1.1,13)
  d.rect(ox+1,77,458,48,'#253342' if isgood else '#352b35','none',0,12)
  d.circle(ox+25,100,9,GREEN if isgood else RED,'none',0)
  d.text(ox+47,106,label_ok if isgood else label_bad,WHITE,16,700)
  d.add(f'<g transform="translate({ox+13},130)">')
  scene(key,d,isgood)
  d.add('</g>')
  d.line(ox+16,348,ox+443,348,LINE,1)
  words=caption_lines(desc_good if isgood else desc_bad,46)
  for i,s in enumerate(words):d.text(ox+21,373+i*19,s,DIM,14,500)
  if isgood:d.tick(ox+426,369)
  else:d.x(ox+427,367,RED,8)
 return '<?xml version="1.0" encoding="UTF-8"?>\n'+f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 440" role="img" aria-label="{escape(key)}">\n'+''.join(d.a)+'</svg>\n'


def main():
 keys=[]
 for file in sorted(CONTENT.glob('*.json')):
  if file.name=='manifest.json':continue
  obj=json.loads(file.read_text(encoding='utf8'))
  keys.append(obj['key'])
 assert len(keys)==36 and set(keys)==set(LABELS), (set(keys)-set(LABELS),set(LABELS)-set(keys))
 for lang in ['ru','en']:
  dest=OUT/lang;dest.mkdir(parents=True,exist_ok=True)
  for key in keys:
   ix=0 if lang=='ru' else 1
   (dest/(key.replace('_','-')+'.svg')).write_text(render(key,lang,LABELS[key][ix]),encoding='utf8')
 print('Generated',2*len(keys),'localized SVG diagrams')

if __name__=='__main__':main()

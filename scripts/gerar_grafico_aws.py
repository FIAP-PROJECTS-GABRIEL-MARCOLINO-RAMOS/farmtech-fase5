"""Recalcula subtotais da cotação registrada e gera o gráfico do README."""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import csv
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
quote = json.loads((ROOT / 'document/aws-cotacao.json').read_text())
rows = []
for region in quote['regioes']:
    ec2 = Decimal(str(region['ec2_usd_hora'])) * quote['horas_mes']
    ebs = Decimal(str(region['ebs_usd_gb_mes'])) * quote['armazenamento_gb_calculadora']
    rounded = lambda v: str(v.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
    rows.append({'regiao':region['nome'], 'codigo':region['codigo'],
                 'EC2_USD_mes':rounded(ec2), 'EBS_USD_mes':rounded(ebs),
                 'subtotal_USD_mes':rounded(ec2+ebs)})
with (ROOT / 'document/aws-custos.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
fig, ax = plt.subplots(figsize=(9, 4.7), layout='constrained')
names = [r['regiao'] for r in rows]
ec2_values = [float(r['EC2_USD_mes']) for r in rows]
ebs_values = [float(r['EBS_USD_mes']) for r in rows]
ax.barh(names, ec2_values, color='#196c59', label='EC2 Linux · 730 h')
ax.barh(names, ebs_values, left=ec2_values, color='#e8b350', label='EBS magnético · 50 GB')
for i, r in enumerate(rows):
    ax.text(float(r['subtotal_USD_mes']) + .2, i, f"US$ {r['subtotal_USD_mes']}", va='center', weight='bold')
ax.set(xlim=(0,19), xlabel='Subtotal mensal (USD)',
       title='FarmTech · mesma máquina, duas regiões\nt4g.micro · On-Demand 100% · cotação de 08/09/2026')
ax.spines[['top','right']].set_visible(False)
ax.legend(loc='lower right')
fig.text(.02,-.035,'Subtotal de computação e capacidade de disco. I/O, IPv4, tráfego, impostos e demais itens excluídos.',fontsize=9)
fig.savefig(ROOT / 'assets/aws/custos-regioes.png', dpi=160, bbox_inches='tight')
print(rows)

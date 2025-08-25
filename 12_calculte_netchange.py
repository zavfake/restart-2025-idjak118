preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Devide the preproInsulin into 4 categories amino acid
lsInsulin = preproInsulin[0:24]
bInsulin = preproInsulin[24:54]
cInsulin = preproInsulin[54:89]
aInsulin = preproInsulin[89:110]
insulin = bInsulin + aInsulin

# Evaluate the result
print(f'{lsInsulin} len {len(lsInsulin)}')
print(f'{bInsulin} len {len(bInsulin)}')
print(f'{cInsulin} len {len(cInsulin)}')
print(f'{aInsulin} len {len(aInsulin)}')

print("=== insulin ===")
print(f'{insulin} len {len(insulin)}')


pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25
}

seqCount = ({x: float(insulin.count(x)) for x in pKR.keys()})

pH = 0
while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values())))
    seqCount = ({x: float(insulin.count(x)) for x in pKR.keys()})
    print('{0:.2f}'.format(pH), netCharge)
    pH+=1

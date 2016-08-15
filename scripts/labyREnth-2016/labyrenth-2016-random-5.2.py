#!/usr/bin/env python

import dis

buf = '650064016e01196e015a026e0164026e0109640a096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096403096e0109196e01095a02096e01096402096e01096404096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096405096e0109196e01095a02096e01096402096e01096406096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096407096e0109196e01095a02096e01096402096e01096408096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096409096e0109196e01095a02096e01096402096e0109640c096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e0109640d096e0109196e01095a02096e01096402096e0109640e096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e0109640f096e0109196e01095a02096e01096402096e01096410096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096411096e0109196e01095a02096e01096402096e01096412096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096413096e0109196e01095a02096e01096402096e01096414096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096415096e0109196e01095a02096e01096402096e01096416096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096417096e0109196e01095a02096e01096402096e01096418096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096419096e0109196e01095a02096e01096402096e0109641a096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e0109641b096e0109196e01095a02096e01096402096e0109641c096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e0109641d096e0109196e01095a02096e01096402096e0109641e096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096501096e01096500096e0109641f096e0109196e01095a02096e01096402096e01096420096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096421096e0109196e01095a02096e01096402096e01096422096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096423096e0109196e01095a02096e01096402096e01096424096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096425096e0109196e01095a02096e01096402096e01096426096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096427096e0109196e01095a02096e01096402096e01096428096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096429096e0109196e01095a02096e01096402096e0109642a096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e0109642b096e0109196e01095a02096e01096402096e0109642c096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e0109642d096e0109196e01095a02096e01096402096e0109642e096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e0109642f096e0109196e01095a02096e01096402096e01096430096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096431096e0109196e01095a02096e01096402096e01096432096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e01096500096e01096433096e0109196e01095a02096e01096402096e01096434096e0109196e01095a03096e0109640b096e01096400096e0109046e0109556e01096501096e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e0109406e01095a01096e01096400096e0109536e0109fdff6e45cd'

newBuf = [int(buf[x:x+2], 16) for x in range(0, len(buf), 2)]

for op in newBuf:
	print dis.opname[op]
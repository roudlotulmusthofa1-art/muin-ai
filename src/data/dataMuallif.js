// Data dummy mu'allif. tahunWafat dipakai untuk mengurutkan (wafat terdahulu dulu).
export const dataMuallif = [
  { id: 'qadim', nama: 'Mu’allif Demo al-Qadim', keterangan: 'w. 450 H', tahunWafat: 450 },
  { id: 'wasit', nama: 'Mu’allif Demo al-Wasit', keterangan: 'w. 505 H', tahunWafat: 505 },
  { id: 'mutaakhkhir', nama: 'Mu’allif Demo al-Muta’akhkhir', keterangan: 'w. 676 H', tahunWafat: 676 },
  { id: 'rabi', nama: 'Mu’allif Demo al-Rabi’', keterangan: 'w. 974 H', tahunWafat: 974 },
  { id: 'kontemporer', nama: 'Mu’allif Demo Kontemporer', keterangan: 'Kontemporer · معاصر', tahunWafat: 9999 },
]

export function namaMuallif(id) {
  return dataMuallif.find((m) => m.id === id)?.nama ?? ''
}

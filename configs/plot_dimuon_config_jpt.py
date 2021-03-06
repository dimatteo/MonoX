import ROOT as r
directory = "category_resolved"
signals = {	 
           # "signal_ggH": ["ggH",r.kAzure+10	,0] 
           #,"signal_vbf": ["VBF",r.kRed	,0] 
	   }

key_order = ["Dibosons","Top","Z#rightarrow #mu#mu"]

backgrounds = { 
		"Top":			  [["dimuon_topjet1pt"],		r.kRed+1,   0]
		,"Dibosons":		  [["dimuon_dibosonsjet1pt"],		r.kGray,   0]
		,"Z#rightarrow #mu#mu":	  [["corrected_dimuon_zlljet1pt"],		r.kGreen+3,   0]
		#,"Z#rightarrow #mu#mu":	  [["dimuon_zll"],	r.kGreen+3,   0]
		#,"QCD":	  		  [["dimuon_qcd"],		r.kRed+2,   0]

	      }

dataname  = "dimuon_datajet1pt"

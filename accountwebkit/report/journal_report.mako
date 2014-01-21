<html>
<head>
	<style type="text/css">${css}</style>
</head>
<body>
	<h1>Journal Report</h1>
	% for iten in objects:
	<h2>${iten.journal_id.name} - ${iten.name}</h2>
	<p>From ${formatLang(iten.end_date, date=True)} to
		${formatLang(iten.end_date, date=True)}.</p>
	<p>Partner:
		<ul>
			% for partner in iten.partner_id:
				<li>${partner.partner_id.name}</li>
			% endfor
		</ul>
	</p>
	% endfor
</body>
</html>
import unittest

from linear_model import LinearRegression, PARegressor

class TestLinearRegression(unittest.TestCase):
    data = '{"id":0, "tp":2,"result":[{"k":[1651086000],"v":[25822]},{"k":[1651089600],"v":[26091]},{"k":[1651093200],"v":[25980]},{"k":[1651096800],"v":[25786]},{"k":[1651100400],"v":[25906]},{"k":[1651104000],"v":[25932]},{"k":[1651107600],"v":[24827]},{"k":[1651111200],"v":[25810]},{"k":[1651114800],"v":[25179]},{"k":[1651118400],"v":[25968]},{"k":[1651122000],"v":[26106]},{"k":[1651125600],"v":[26213]},{"k":[1651129200],"v":[26208]},{"k":[1651132800],"v":[26158]},{"k":[1651136400],"v":[26621]},{"k":[1651140000],"v":[33805]},{"k":[1651143600],"v":[28003]},{"k":[1651147200],"v":[27051]},{"k":[1651150800],"v":[25901]},{"k":[1651154400],"v":[26336]},{"k":[1651158000],"v":[27481]},{"k":[1651161600],"v":[26075]},{"k":[1651165200],"v":[26228]},{"k":[1651168800],"v":[27198]},{"k":[1651172400],"v":[26028]},{"k":[1651176000],"v":[25933]},{"k":[1651179600],"v":[26360]},{"k":[1651183200],"v":[25950]},{"k":[1651186800],"v":[26032]},{"k":[1651190400],"v":[26172]},{"k":[1651194000],"v":[25888]},{"k":[1651197600],"v":[26247]},{"k":[1651201200],"v":[25965]},{"k":[1651204800],"v":[25995]},{"k":[1651208400],"v":[26085]},{"k":[1651212000],"v":[25952]},{"k":[1651215600],"v":[26553]},{"k":[1651219200],"v":[26298]},{"k":[1651222800],"v":[29003]},{"k":[1651226400],"v":[26286]},{"k":[1651230000],"v":[34678]},{"k":[1651233600],"v":[32144]},{"k":[1651237200],"v":[35580]},{"k":[1651240800],"v":[31577]},{"k":[1651244400],"v":[25735]},{"k":[1651248000],"v":[25803]},{"k":[1651251600],"v":[27415]},{"k":[1651255200],"v":[27623]},{"k":[1651258800],"v":[27752]},{"k":[1651262400],"v":[27870]},{"k":[1651266000],"v":[27766]},{"k":[1651269600],"v":[27633]},{"k":[1651273200],"v":[28722]},{"k":[1651276800],"v":[25958]},{"k":[1651280400],"v":[25933]},{"k":[1651284000],"v":[26108]},{"k":[1651287600],"v":[25999]},{"k":[1651291200],"v":[26105]},{"k":[1651294800],"v":[26279]},{"k":[1651298400],"v":[26922]},{"k":[1651302000],"v":[26272]},{"k":[1651305600],"v":[26373]},{"k":[1651309200],"v":[26091]},{"k":[1651312800],"v":[26865]},{"k":[1651316400],"v":[26115]},{"k":[1651320000],"v":[26516]},{"k":[1651323600],"v":[26097]},{"k":[1651327200],"v":[26051]},{"k":[1651330800],"v":[26344]},{"k":[1651334400],"v":[26018]},{"k":[1651338000],"v":[26509]},{"k":[1651341600],"v":[26654]},{"k":[1651345200],"v":[26250]},{"k":[1651348800],"v":[26119]},{"k":[1651352400],"v":[26273]},{"k":[1651356000],"v":[26217]},{"k":[1651359600],"v":[26142]},{"k":[1651363200],"v":[25993]},{"k":[1651366800],"v":[26019]},{"k":[1651370400],"v":[26138]},{"k":[1651374000],"v":[25919]},{"k":[1651377600],"v":[26000]},{"k":[1651381200],"v":[26043]},{"k":[1651384800],"v":[26505]},{"k":[1651388400],"v":[26474]},{"k":[1651392000],"v":[26758]},{"k":[1651395600],"v":[27063]},{"k":[1651399200],"v":[25895]},{"k":[1651402800],"v":[25972]},{"k":[1651406400],"v":[25965]},{"k":[1651410000],"v":[25778]},{"k":[1651413600],"v":[25962]},{"k":[1651417200],"v":[25788]},{"k":[1651420800],"v":[26128]},{"k":[1651424400],"v":[25651]},{"k":[1651428000],"v":[25876]},{"k":[1651431600],"v":[25957]},{"k":[1651435200],"v":[25819]},{"k":[1651438800],"v":[26025]},{"k":[1651442400],"v":[25622]},{"k":[1651446000],"v":[25698]},{"k":[1651449600],"v":[25841]},{"k":[1651453200],"v":[25903]},{"k":[1651456800],"v":[25710]},{"k":[1651460400],"v":[25431]},{"k":[1651464000],"v":[24847]},{"k":[1651467600],"v":[25128]},{"k":[1651471200],"v":[24918]},{"k":[1651474800],"v":[26583]},{"k":[1651478400],"v":[26068]},{"k":[1651482000],"v":[26258]},{"k":[1651485600],"v":[26191]},{"k":[1651489200],"v":[28446]},{"k":[1651492800],"v":[26312]},{"k":[1651496400],"v":[26367]},{"k":[1651500000],"v":[29336]},{"k":[1651503600],"v":[26199]},{"k":[1651507200],"v":[71608]},{"k":[1651510800],"v":[25858]},{"k":[1651514400],"v":[26278]},{"k":[1651518000],"v":[26277]},{"k":[1651521600],"v":[25930]},{"k":[1651525200],"v":[26224]},{"k":[1651528800],"v":[26144]},{"k":[1651532400],"v":[26060]},{"k":[1651536000],"v":[25871]},{"k":[1651539600],"v":[26061]},{"k":[1651543200],"v":[25959]},{"k":[1651546800],"v":[26189]},{"k":[1651550400],"v":[26175]},{"k":[1651554000],"v":[26125]},{"k":[1651557600],"v":[25994]},{"k":[1651561200],"v":[25992]},{"k":[1651564800],"v":[26048]},{"k":[1651568400],"v":[26205]},{"k":[1651572000],"v":[29539]},{"k":[1651575600],"v":[25935]},{"k":[1651579200],"v":[26041]},{"k":[1651582800],"v":[25995]},{"k":[1651586400],"v":[26425]},{"k":[1651590000],"v":[25955]},{"k":[1651593600],"v":[33179]},{"k":[1651597200],"v":[26030]},{"k":[1651600800],"v":[25968]},{"k":[1651604400],"v":[26028]},{"k":[1651608000],"v":[31201]},{"k":[1651611600],"v":[72334]},{"k":[1651615200],"v":[32202]},{"k":[1651618800],"v":[25085]},{"k":[1651622400],"v":[27102]},{"k":[1651626000],"v":[25237]},{"k":[1651629600],"v":[25010]},{"k":[1651633200],"v":[24958]},{"k":[1651636800],"v":[24951]},{"k":[1651640400],"v":[25028]},{"k":[1651644000],"v":[27805]},{"k":[1651647600],"v":[41229]},{"k":[1651651200],"v":[66383]},{"k":[1651654800],"v":[119174]},{"k":[1651658400],"v":[127351]},{"k":[1651662000],"v":[32235]},{"k":[1651665600],"v":[25382]},{"k":[1651669200],"v":[26001]},{"k":[1651672800],"v":[24935]},{"k":[1651676400],"v":[25108]},{"k":[1651680000],"v":[25248]},{"k":[1651683600],"v":[24572]},{"k":[1651687200],"v":[25534]},{"k":[1651690800],"v":[25000]},{"k":[1651694400],"v":[24975]},{"k":[1651698000],"v":[25008]},{"k":[1651701600],"v":[25056]},{"k":[1651705200],"v":[25056]},{"k":[1651708800],"v":[25175]},{"k":[1651712400],"v":[25038]},{"k":[1651716000],"v":[25018]},{"k":[1651719600],"v":[25038]},{"k":[1651723200],"v":[25178]},{"k":[1651726800],"v":[25182]},{"k":[1651730400],"v":[24382]},{"k":[1651734000],"v":[25113]},{"k":[1651737600],"v":[25038]},{"k":[1651741200],"v":[24481]},{"k":[1651744800],"v":[25152]},{"k":[1651748400],"v":[25243]},{"k":[1651752000],"v":[24870]},{"k":[1651755600],"v":[26249]},{"k":[1651759200],"v":[25616]},{"k":[1651762800],"v":[24900]},{"k":[1651766400],"v":[24913]},{"k":[1651770000],"v":[24949]},{"k":[1651773600],"v":[25052]},{"k":[1651777200],"v":[24838]},{"k":[1651780800],"v":[24799]},{"k":[1651784400],"v":[24919]},{"k":[1651788000],"v":[24918]},{"k":[1651791600],"v":[25096]},{"k":[1651795200],"v":[24905]},{"k":[1651798800],"v":[25149]},{"k":[1651802400],"v":[25186]},{"k":[1651806000],"v":[24997]},{"k":[1651809600],"v":[24974]},{"k":[1651813200],"v":[25155]},{"k":[1651816800],"v":[25365]},{"k":[1651820400],"v":[25038]},{"k":[1651824000],"v":[25428]},{"k":[1651827600],"v":[24976]},{"k":[1651831200],"v":[24978]},{"k":[1651834800],"v":[24950]},{"k":[1651838400],"v":[24999]},{"k":[1651842000],"v":[25010]},{"k":[1651845600],"v":[25064]},{"k":[1651849200],"v":[24928]},{"k":[1651852800],"v":[25034]},{"k":[1651856400],"v":[24766]},{"k":[1651860000],"v":[25060]},{"k":[1651863600],"v":[25184]},{"k":[1651867200],"v":[24904]},{"k":[1651870800],"v":[24864]},{"k":[1651874400],"v":[24902]},{"k":[1651878000],"v":[24863]},{"k":[1651881600],"v":[25111]},{"k":[1651885200],"v":[25194]},{"k":[1651888800],"v":[25261]},{"k":[1651892400],"v":[25115]},{"k":[1651896000],"v":[25088]},{"k":[1651899600],"v":[25036]},{"k":[1651903200],"v":[25191]},{"k":[1651906800],"v":[25154]},{"k":[1651910400],"v":[25027]},{"k":[1651914000],"v":[25138]},{"k":[1651917600],"v":[24778]},{"k":[1651921200],"v":[25023]},{"k":[1651924800],"v":[26219]},{"k":[1651928400],"v":[25617]},{"k":[1651932000],"v":[25247]},{"k":[1651935600],"v":[24846]},{"k":[1651939200],"v":[24907]},{"k":[1651942800],"v":[25166]},{"k":[1651946400],"v":[25112]},{"k":[1651950000],"v":[24904]},{"k":[1651953600],"v":[24998]},{"k":[1651957200],"v":[24836]},{"k":[1651960800],"v":[24866]},{"k":[1651964400],"v":[25019]},{"k":[1651968000],"v":[24981]},{"k":[1651971600],"v":[25148]},{"k":[1651975200],"v":[24814]},{"k":[1651978800],"v":[24957]},{"k":[1651982400],"v":[24866]},{"k":[1651986000],"v":[24839]},{"k":[1651989600],"v":[25048]},{"k":[1651993200],"v":[25048]},{"k":[1651996800],"v":[25044]},{"k":[1652000400],"v":[24974]},{"k":[1652004000],"v":[24187]},{"k":[1652007600],"v":[24934]},{"k":[1652011200],"v":[25076]},{"k":[1652014800],"v":[24967]},{"k":[1652018400],"v":[24848]},{"k":[1652022000],"v":[25018]},{"k":[1652025600],"v":[25012]},{"k":[1652029200],"v":[24974]},{"k":[1652032800],"v":[24825]},{"k":[1652036400],"v":[25060]},{"k":[1652040000],"v":[25016]},{"k":[1652043600],"v":[24980]},{"k":[1652047200],"v":[24969]},{"k":[1652050800],"v":[24965]},{"k":[1652054400],"v":[24786]},{"k":[1652058000],"v":[25602]},{"k":[1652061600],"v":[23689]},{"k":[1652065200],"v":[24488]},{"k":[1652068800],"v":[25572]},{"k":[1652072400],"v":[24848]},{"k":[1652076000],"v":[25658]},{"k":[1652079600],"v":[27547]},{"k":[1652083200],"v":[42215]},{"k":[1652086800],"v":[29708]},{"k":[1652090400],"v":[35048]},{"k":[1652094000],"v":[66011]},{"k":[1652097600],"v":[55030]},{"k":[1652101200],"v":[61469]},{"k":[1652104800],"v":[89634]},{"k":[1652108400],"v":[59686]},{"k":[1652112000],"v":[24318]},{"k":[1652115600],"v":[24928]},{"k":[1652119200],"v":[25005]},{"k":[1652122800],"v":[27220]},{"k":[1652126400],"v":[35786]},{"k":[1652130000],"v":[25150]},{"k":[1652133600],"v":[24881]},{"k":[1652137200],"v":[25023]},{"k":[1652140800],"v":[25018]},{"k":[1652144400],"v":[25078]},{"k":[1652148000],"v":[24403]},{"k":[1652151600],"v":[24898]},{"k":[1652155200],"v":[25038]},{"k":[1652158800],"v":[24976]},{"k":[1652162400],"v":[24932]},{"k":[1652166000],"v":[24989]},{"k":[1652169600],"v":[24928]},{"k":[1652173200],"v":[24995]},{"k":[1652176800],"v":[26112]},{"k":[1652180400],"v":[29780]},{"k":[1652184000],"v":[24867]},{"k":[1652187600],"v":[24922]},{"k":[1652191200],"v":[35503]},{"k":[1652194800],"v":[40787]},{"k":[1652198400],"v":[122653]},{"k":[1652202000],"v":[65330]},{"k":[1652205600],"v":[62199]},{"k":[1652209200],"v":[45622]},{"k":[1652212800],"v":[44496]},{"k":[1652216400],"v":[44390]},{"k":[1652220000],"v":[44254]},{"k":[1652223600],"v":[44462]},{"k":[1652227200],"v":[44299]},{"k":[1652230800],"v":[44211]},{"k":[1652234400],"v":[44339]},{"k":[1652238000],"v":[44307]},{"k":[1652241600],"v":[44338]},{"k":[1652245200],"v":[44423]},{"k":[1652248800],"v":[44255]},{"k":[1652252400],"v":[59009]},{"k":[1652256000],"v":[57688]},{"k":[1652259600],"v":[59451]},{"k":[1652263200],"v":[27558]},{"k":[1652266800],"v":[25581]},{"k":[1652270400],"v":[25390]},{"k":[1652274000],"v":[27819]},{"k":[1652277600],"v":[24969]},{"k":[1652281200],"v":[28631]},{"k":[1652284800],"v":[31358]},{"k":[1652288400],"v":[25855]},{"k":[1652292000],"v":[25297]},{"k":[1652295600],"v":[24890]},{"k":[1652299200],"v":[25048]},{"k":[1652302800],"v":[25895]},{"k":[1652306400],"v":[25112]},{"k":[1652310000],"v":[25975]},{"k":[1652313600],"v":[26570]},{"k":[1652317200],"v":[26604]},{"k":[1652320800],"v":[26936]},{"k":[1652324400],"v":[26579]},{"k":[1652328000],"v":[27068]},{"k":[1652331600],"v":[26637]},{"k":[1652335200],"v":[25693]},{"k":[1652338800],"v":[25396]},{"k":[1652342400],"v":[25405]},{"k":[1652346000],"v":[25308]},{"k":[1652349600],"v":[48450]},{"k":[1652353200],"v":[36990]},{"k":[1652356800],"v":[25554]},{"k":[1652360400],"v":[30448]},{"k":[1652364000],"v":[37838]},{"k":[1652367600],"v":[38183]},{"k":[1652371200],"v":[32752]},{"k":[1652374800],"v":[25462]},{"k":[1652378400],"v":[25406]},{"k":[1652382000],"v":[25447]},{"k":[1652385600],"v":[25082]},{"k":[1652389200],"v":[24906]},{"k":[1652392800],"v":[25200]},{"k":[1652396400],"v":[24184]},{"k":[1652400000],"v":[23705]},{"k":[1652403600],"v":[23807]},{"k":[1652407200],"v":[23712]},{"k":[1652410800],"v":[23711]},{"k":[1652414400],"v":[23934]},{"k":[1652418000],"v":[23758]},{"k":[1652421600],"v":[25249]},{"k":[1652425200],"v":[25353]},{"k":[1652428800],"v":[31674]},{"k":[1652432400],"v":[32686]},{"k":[1652436000],"v":[30125]},{"k":[1652439600],"v":[32289]},{"k":[1652443200],"v":[25050]},{"k":[1652446800],"v":[38349]},{"k":[1652450400],"v":[32409]},{"k":[1652454000],"v":[25202]},{"k":[1652457600],"v":[24971]},{"k":[1652461200],"v":[25240]},{"k":[1652464800],"v":[26465]},{"k":[1652468400],"v":[26534]},{"k":[1652472000],"v":[26624]},{"k":[1652475600],"v":[26629]},{"k":[1652479200],"v":[26478]},{"k":[1652482800],"v":[26491]},{"k":[1652486400],"v":[26207]},{"k":[1652490000],"v":[26384]},{"k":[1652493600],"v":[26696]},{"k":[1652497200],"v":[25727]},{"k":[1652500800],"v":[26595]},{"k":[1652504400],"v":[26072]},{"k":[1652508000],"v":[26758]},{"k":[1652511600],"v":[26751]},{"k":[1652515200],"v":[27142]},{"k":[1652518800],"v":[26919]},{"k":[1652522400],"v":[25696]},{"k":[1652526000],"v":[25356]},{"k":[1652529600],"v":[25105]},{"k":[1652533200],"v":[25252]},{"k":[1652536800],"v":[25657]},{"k":[1652540400],"v":[25630]},{"k":[1652544000],"v":[24682]},{"k":[1652547600],"v":[25322]},{"k":[1652551200],"v":[24304]},{"k":[1652554800],"v":[24731]},{"k":[1652558400],"v":[24233]},{"k":[1652562000],"v":[23616]},{"k":[1652565600],"v":[24116]},{"k":[1652569200],"v":[24865]},{"k":[1652572800],"v":[24388]},{"k":[1652576400],"v":[24952]},{"k":[1652580000],"v":[24276]},{"k":[1652583600],"v":[24975]},{"k":[1652587200],"v":[26512]},{"k":[1652590800],"v":[25053]},{"k":[1652594400],"v":[25903]},{"k":[1652598000],"v":[24862]},{"k":[1652601600],"v":[25032]},{"k":[1652605200],"v":[25887]},{"k":[1652608800],"v":[24659]},{"k":[1652612400],"v":[25132]},{"k":[1652616000],"v":[25000]},{"k":[1652619600],"v":[25214]},{"k":[1652623200],"v":[24998]},{"k":[1652626800],"v":[24139]},{"k":[1652630400],"v":[24928]},{"k":[1652634000],"v":[25040]},{"k":[1652637600],"v":[24960]},{"k":[1652641200],"v":[25268]},{"k":[1652644800],"v":[23652]},{"k":[1652648400],"v":[23888]},{"k":[1652652000],"v":[23758]},{"k":[1652655600],"v":[23785]},{"k":[1652659200],"v":[23617]},{"k":[1652662800],"v":[23408]},{"k":[1652666400],"v":[25102]},{"k":[1652670000],"v":[24878]},{"k":[1652673600],"v":[24875]},{"k":[1652677200],"v":[25881]},{"k":[1652680800],"v":[25008]},{"k":[1652684400],"v":[26392]},{"k":[1652688000],"v":[40233]},{"k":[1652691600],"v":[40485]},{"k":[1652695200],"v":[58399]},{"k":[1652698800],"v":[65635]},{"k":[1652702400],"v":[85413]},{"k":[1652706000],"v":[37484]},{"k":[1652709600],"v":[28367]},{"k":[1652713200],"v":[44309]},{"k":[1652716800],"v":[41643]},{"k":[1652720400],"v":[26673]},{"k":[1652724000],"v":[26533]},{"k":[1652727600],"v":[30552]},{"k":[1652731200],"v":[31593]},{"k":[1652734800],"v":[31829]},{"k":[1652738400],"v":[33246]},{"k":[1652742000],"v":[32865]},{"k":[1652745600],"v":[33579]},{"k":[1652749200],"v":[35035]},{"k":[1652752800],"v":[32810]},{"k":[1652756400],"v":[35172]},{"k":[1652760000],"v":[35443]},{"k":[1652763600],"v":[36768]},{"k":[1652767200],"v":[37058]},{"k":[1652770800],"v":[35735]},{"k":[1652774400],"v":[72424]},{"k":[1652778000],"v":[71247]},{"k":[1652781600],"v":[28242]},{"k":[1652785200],"v":[27011]},{"k":[1652788800],"v":[24643]},{"k":[1652792400],"v":[27925]},{"k":[1652796000],"v":[43177]},{"k":[1652799600],"v":[28742]},{"k":[1652803200],"v":[24975]},{"k":[1652806800],"v":[25249]},{"k":[1652810400],"v":[24997]},{"k":[1652814000],"v":[25073]},{"k":[1652817600],"v":[25527]},{"k":[1652821200],"v":[25198]},{"k":[1652824800],"v":[25251]},{"k":[1652828400],"v":[25267]},{"k":[1652832000],"v":[26222]},{"k":[1652835600],"v":[25216]},{"k":[1652839200],"v":[25164]},{"k":[1652842800],"v":[26092]},{"k":[1652846400],"v":[26661]},{"k":[1652850000],"v":[26971]},{"k":[1652853600],"v":[26727]},{"k":[1652857200],"v":[26651]},{"k":[1652860800],"v":[25725]},{"k":[1652864400],"v":[26374]},{"k":[1652868000],"v":[26934]},{"k":[1652871600],"v":[27254]},{"k":[1652875200],"v":[26535]},{"k":[1652878800],"v":[28815]},{"k":[1652882400],"v":[40000]},{"k":[1652886000],"v":[38629]},{"k":[1652889600],"v":[41902]},{"k":[1652893200],"v":[25848]},{"k":[1652896800],"v":[26263]},{"k":[1652900400],"v":[26148]},{"k":[1652904000],"v":[26862]},{"k":[1652907600],"v":[26652]},{"k":[1652911200],"v":[26133]},{"k":[1652914800],"v":[26568]},{"k":[1652918400],"v":[27092]},{"k":[1652922000],"v":[26582]},{"k":[1652925600],"v":[26492]},{"k":[1652929200],"v":[26489]},{"k":[1652932800],"v":[26482]},{"k":[1652936400],"v":[26732]},{"k":[1652940000],"v":[26502]},{"k":[1652943600],"v":[26572]},{"k":[1652947200],"v":[32894]},{"k":[1652950800],"v":[26702]},{"k":[1652954400],"v":[31475]},{"k":[1652958000],"v":[26374]},{"k":[1652961600],"v":[26356]},{"k":[1652965200],"v":[26529]},{"k":[1652968800],"v":[33811]},{"k":[1652972400],"v":[27303]},{"k":[1652976000],"v":[27865]},{"k":[1652979600],"v":[26062]},{"k":[1652983200],"v":[25381]},{"k":[1652986800],"v":[26694]},{"k":[1652990400],"v":[24965]},{"k":[1652994000],"v":[25127]},{"k":[1652997600],"v":[24998]},{"k":[1653001200],"v":[24953]},{"k":[1653004800],"v":[25062]},{"k":[1653008400],"v":[26187]},{"k":[1653012000],"v":[25677]},{"k":[1653015600],"v":[25645]},{"k":[1653019200],"v":[25756]},{"k":[1653022800],"v":[27448]},{"k":[1653026400],"v":[25642]},{"k":[1653030000],"v":[27018]},{"k":[1653033600],"v":[26097]},{"k":[1653037200],"v":[29608]},{"k":[1653040800],"v":[25897]},{"k":[1653044400],"v":[29191]},{"k":[1653048000],"v":[25021]},{"k":[1653051600],"v":[25980]},{"k":[1653055200],"v":[25680]},{"k":[1653058800],"v":[24900]},{"k":[1653062400],"v":[25136]},{"k":[1653066000],"v":[24983]},{"k":[1653069600],"v":[24654]},{"k":[1653073200],"v":[24957]},{"k":[1653076800],"v":[24438]},{"k":[1653080400],"v":[25022]},{"k":[1653084000],"v":[25012]},{"k":[1653087600],"v":[25201]},{"k":[1653091200],"v":[24987]},{"k":[1653094800],"v":[24961]},{"k":[1653098400],"v":[24971]},{"k":[1653102000],"v":[25341]},{"k":[1653105600],"v":[25138]},{"k":[1653109200],"v":[25379]},{"k":[1653112800],"v":[25056]},{"k":[1653116400],"v":[24982]},{"k":[1653120000],"v":[25172]},{"k":[1653123600],"v":[24676]},{"k":[1653127200],"v":[24865]},{"k":[1653130800],"v":[24465]},{"k":[1653134400],"v":[24525]},{"k":[1653138000],"v":[25058]},{"k":[1653141600],"v":[24970]},{"k":[1653145200],"v":[24962]},{"k":[1653148800],"v":[24965]},{"k":[1653152400],"v":[24493]},{"k":[1653156000],"v":[25041]},{"k":[1653159600],"v":[24977]},{"k":[1653163200],"v":[24959]},{"k":[1653166800],"v":[26260]},{"k":[1653170400],"v":[25070]},{"k":[1653174000],"v":[25061]},{"k":[1653177600],"v":[25341]},{"k":[1653181200],"v":[25061]},{"k":[1653184800],"v":[25092]},{"k":[1653188400],"v":[24445]},{"k":[1653192000],"v":[24930]},{"k":[1653195600],"v":[25276]},{"k":[1653199200],"v":[25344]},{"k":[1653202800],"v":[24660]},{"k":[1653206400],"v":[24732]},{"k":[1653210000],"v":[25254]},{"k":[1653213600],"v":[24751]},{"k":[1653217200],"v":[25215]},{"k":[1653220800],"v":[24963]},{"k":[1653224400],"v":[24952]},{"k":[1653228000],"v":[25056]},{"k":[1653231600],"v":[25748]},{"k":[1653235200],"v":[25130]},{"k":[1653238800],"v":[25051]},{"k":[1653242400],"v":[25847]},{"k":[1653246000],"v":[27198]},{"k":[1653249600],"v":[25025]},{"k":[1653253200],"v":[26032]},{"k":[1653256800],"v":[24998]},{"k":[1653260400],"v":[26051]},{"k":[1653264000],"v":[24996]},{"k":[1653267600],"v":[24998]},{"k":[1653271200],"v":[25067]},{"k":[1653274800],"v":[25188]},{"k":[1653278400],"v":[25158]},{"k":[1653282000],"v":[24998]},{"k":[1653285600],"v":[25436]},{"k":[1653289200],"v":[25165]},{"k":[1653292800],"v":[25542]},{"k":[1653296400],"v":[25656]},{"k":[1653300000],"v":[25972]},{"k":[1653303600],"v":[28448]},{"k":[1653307200],"v":[28042]},{"k":[1653310800],"v":[29287]},{"k":[1653314400],"v":[29795]},{"k":[1653318000],"v":[31366]},{"k":[1653321600],"v":[29682]},{"k":[1653325200],"v":[25329]},{"k":[1653328800],"v":[24281]},{"k":[1653332400],"v":[25169]},{"k":[1653336000],"v":[25219]},{"k":[1653339600],"v":[25364]},{"k":[1653343200],"v":[25232]},{"k":[1653346800],"v":[24994]},{"k":[1653350400],"v":[25060]},{"k":[1653354000],"v":[24422]},{"k":[1653357600],"v":[24444]},{"k":[1653361200],"v":[25233]},{"k":[1653364800],"v":[25369]},{"k":[1653368400],"v":[25216]},{"k":[1653372000],"v":[25073]},{"k":[1653375600],"v":[27507]},{"k":[1653379200],"v":[27376]},{"k":[1653382800],"v":[28368]},{"k":[1653386400],"v":[26296]},{"k":[1653390000],"v":[25789]},{"k":[1653393600],"v":[24891]},{"k":[1653397200],"v":[25287]},{"k":[1653400800],"v":[26247]},{"k":[1653404400],"v":[25365]},{"k":[1653408000],"v":[25099]},{"k":[1653411600],"v":[24953]},{"k":[1653415200],"v":[24865]},{"k":[1653418800],"v":[25254]},{"k":[1653422400],"v":[27134]},{"k":[1653426000],"v":[27186]},{"k":[1653429600],"v":[27262]},{"k":[1653433200],"v":[26339]},{"k":[1653436800],"v":[25158]},{"k":[1653440400],"v":[26089]},{"k":[1653444000],"v":[26513]},{"k":[1653447600],"v":[26913]},{"k":[1653451200],"v":[26534]},{"k":[1653454800],"v":[27996]},{"k":[1653458400],"v":[26982]},{"k":[1653462000],"v":[26655]},{"k":[1653465600],"v":[29092]},{"k":[1653469200],"v":[26795]},{"k":[1653472800],"v":[30947]},{"k":[1653476400],"v":[26643]},{"k":[1653480000],"v":[26592]},{"k":[1653483600],"v":[29256]},{"k":[1653487200],"v":[43912]},{"k":[1653490800],"v":[51088]},{"k":[1653494400],"v":[29859]},{"k":[1653498000],"v":[26547]},{"k":[1653501600],"v":[26649]},{"k":[1653505200],"v":[26669]},{"k":[1653508800],"v":[26914]},{"k":[1653512400],"v":[26903]},{"k":[1653516000],"v":[26822]},{"k":[1653519600],"v":[26809]},{"k":[1653523200],"v":[27148]},{"k":[1653526800],"v":[26942]},{"k":[1653530400],"v":[27070]},{"k":[1653534000],"v":[26878]},{"k":[1653537600],"v":[27163]},{"k":[1653541200],"v":[27028]},{"k":[1653544800],"v":[26853]},{"k":[1653548400],"v":[27057]},{"k":[1653552000],"v":[26946]},{"k":[1653555600],"v":[27645]},{"k":[1653559200],"v":[27981]},{"k":[1653562800],"v":[30342]},{"k":[1653566400],"v":[26097]},{"k":[1653570000],"v":[27520]},{"k":[1653573600],"v":[26862]},{"k":[1653577200],"v":[36487]},{"k":[1653580800],"v":[27162]},{"k":[1653584400],"v":[27140]},{"k":[1653588000],"v":[26452]},{"k":[1653591600],"v":[26262]},{"k":[1653595200],"v":[26515]},{"k":[1653598800],"v":[27952]},{"k":[1653602400],"v":[26553]},{"k":[1653638400],"v":[26579]},{"k":[1653642000],"v":[27390]},{"k":[1653645600],"v":[27614]},{"k":[1653649200],"v":[27578]},{"k":[1653652800],"v":[28765]},{"k":[1653656400],"v":[34298]},{"k":[1653660000],"v":[30272]},{"k":[1653663600],"v":[26255]},{"k":[1653667200],"v":[25917]},{"k":[1653670800],"v":[26244]},{"k":[1653674400],"v":[27738]},{"k":[1653678000],"v":[27424]},{"k":[1653681600],"v":[26053]},{"k":[1653685200],"v":[26977]},{"k":[1653688800],"v":[28348]},{"k":[1653692400],"v":[26447]},{"k":[1653696000],"v":[27018]},{"k":[1653699600],"v":[27466]},{"k":[1653703200],"v":[27198]},{"k":[1653706800],"v":[26992]},{"k":[1653710400],"v":[26412]},{"k":[1653714000],"v":[25500]},{"k":[1653717600],"v":[25684]},{"k":[1653721200],"v":[26369]},{"k":[1653724800],"v":[25670]},{"k":[1653728400],"v":[25593]},{"k":[1653732000],"v":[25258]},{"k":[1653735600],"v":[25728]},{"k":[1653739200],"v":[25333]},{"k":[1653742800],"v":[25682]},{"k":[1653746400],"v":[25750]},{"k":[1653753600],"v":[25400]},{"k":[1653757200],"v":[25145]},{"k":[1653760800],"v":[25508]},{"k":[1653764400],"v":[25504]},{"k":[1653768000],"v":[25898]},{"k":[1653771600],"v":[25322]},{"k":[1653775200],"v":[25841]},{"k":[1653778800],"v":[26487]},{"k":[1653782400],"v":[26570]},{"k":[1653786000],"v":[26568]},{"k":[1653789600],"v":[26764]},{"k":[1653793200],"v":[26545]},{"k":[1653796800],"v":[26404]},{"k":[1653800400],"v":[26842]},{"k":[1653804000],"v":[26561]},{"k":[1653807600],"v":[27377]},{"k":[1653811200],"v":[26602]},{"k":[1653814800],"v":[26008]},{"k":[1653818400],"v":[26281]},{"k":[1653822000],"v":[26348]},{"k":[1653825600],"v":[26094]},{"k":[1653829200],"v":[26500]},{"k":[1653832800],"v":[25785]},{"k":[1653836400],"v":[26671]},{"k":[1653840000],"v":[26584]},{"k":[1653843600],"v":[26549]},{"k":[1653847200],"v":[26451]},{"k":[1653850800],"v":[26420]},{"k":[1653854400],"v":[26421]},{"k":[1653858000],"v":[26582]},{"k":[1653861600],"v":[26300]},{"k":[1653865200],"v":[26436]},{"k":[1653868800],"v":[26361]},{"k":[1653872400],"v":[27565]},{"k":[1653876000],"v":[26713]},{"k":[1653879600],"v":[26382]},{"k":[1653883200],"v":[26740]},{"k":[1653886800],"v":[26585]},{"k":[1653890400],"v":[26229]},{"k":[1653894000],"v":[26604]},{"k":[1653897600],"v":[27023]},{"k":[1653901200],"v":[26028]},{"k":[1653904800],"v":[26268]},{"k":[1653908400],"v":[26477]},{"k":[1653912000],"v":[27158]},{"k":[1653915600],"v":[25374]},{"k":[1653919200],"v":[28422]},{"k":[1653922800],"v":[27604]},{"k":[1653926400],"v":[29065]},{"k":[1653930000],"v":[26401]},{"k":[1653933600],"v":[26784]},{"k":[1653937200],"v":[27153]},{"k":[1653940800],"v":[30933]},{"k":[1653944400],"v":[28273]},{"k":[1653948000],"v":[26091]},{"k":[1653951600],"v":[26717]},{"k":[1653955200],"v":[26716]},{"k":[1653958800],"v":[27669]},{"k":[1653962400],"v":[26430]},{"k":[1653966000],"v":[26445]},{"k":[1653969600],"v":[26636]},{"k":[1653973200],"v":[26957]},{"k":[1653976800],"v":[26896]},{"k":[1653980400],"v":[27304]},{"k":[1653984000],"v":[33691]},{"k":[1653987600],"v":[37069]},{"k":[1653991200],"v":[35383]},{"k":[1653994800],"v":[38030]},{"k":[1653998400],"v":[43644]},{"k":[1654002000],"v":[38205]},{"k":[1654005600],"v":[31425]},{"k":[1654009200],"v":[30242]},{"k":[1654012800],"v":[27787]},{"k":[1654016400],"v":[28626]},{"k":[1654020000],"v":[26994]},{"k":[1654023600],"v":[27644]},{"k":[1654027200],"v":[28164]},{"k":[1654030800],"v":[27637]},{"k":[1654034400],"v":[27758]},{"k":[1654038000],"v":[27726]},{"k":[1654041600],"v":[27896]},{"k":[1654045200],"v":[28218]},{"k":[1654048800],"v":[25561]},{"k":[1654052400],"v":[26913]},{"k":[1654056000],"v":[26629]},{"k":[1654059600],"v":[26827]},{"k":[1654063200],"v":[26380]},{"k":[1654066800],"v":[27071]},{"k":[1654070400],"v":[26968]},{"k":[1654074000],"v":[29558]},{"k":[1654077600],"v":[25906]},{"k":[1654081200],"v":[25347]},{"k":[1654084800],"v":[25092]},{"k":[1654088400],"v":[26114]},{"k":[1654092000],"v":[26670]},{"k":[1654095600],"v":[26051]},{"k":[1654099200],"v":[26743]},{"k":[1654102800],"v":[26345]},{"k":[1654106400],"v":[26718]},{"k":[1654110000],"v":[26043]},{"k":[1654113600],"v":[26464]},{"k":[1654117200],"v":[30713]},{"k":[1654120800],"v":[26682]},{"k":[1654124400],"v":[27637]},{"k":[1654128000],"v":[26512]},{"k":[1654131600],"v":[26872]},{"k":[1654135200],"v":[26820]},{"k":[1654138800],"v":[26617]},{"k":[1654142400],"v":[26698]},{"k":[1654146000],"v":[27324]},{"k":[1654149600],"v":[26776]},{"k":[1654153200],"v":[26315]},{"k":[1654156800],"v":[26665]},{"k":[1654160400],"v":[35258]},{"k":[1654164000],"v":[51795]},{"k":[1654167600],"v":[145424]},{"k":[1654171200],"v":[113632]},{"k":[1654174800],"v":[31025]},{"k":[1654178400],"v":[29573]},{"k":[1654182000],"v":[42079]},{"k":[1654185600],"v":[42646]},{"k":[1654189200],"v":[43920]},{"k":[1654192800],"v":[37814]},{"k":[1654196400],"v":[38598]},{"k":[1654200000],"v":[40936]},{"k":[1654203600],"v":[35325]},{"k":[1654207200],"v":[35238]},{"k":[1654210800],"v":[34263]},{"k":[1654214400],"v":[34103]},{"k":[1654218000],"v":[34690]},{"k":[1654221600],"v":[34382]},{"k":[1654225200],"v":[34225]},{"k":[1654228800],"v":[34614]},{"k":[1654232400],"v":[35122]},{"k":[1654236000],"v":[34590]},{"k":[1654239600],"v":[35951]},{"k":[1654243200],"v":[43528]},{"k":[1654246800],"v":[51423]},{"k":[1654250400],"v":[30100]},{"k":[1654254000],"v":[26836]},{"k":[1654257600],"v":[27448]},{"k":[1654261200],"v":[27175]},{"k":[1654264800],"v":[29051]},{"k":[1654268400],"v":[29088]},{"k":[1654272000],"v":[26908]},{"k":[1654275600],"v":[26810]},{"k":[1654279200],"v":[27062]},{"k":[1654282800],"v":[26638]},{"k":[1654286400],"v":[26539]},{"k":[1654290000],"v":[27743]},{"k":[1654293600],"v":[28925]},{"k":[1654297200],"v":[25844]},{"k":[1654300800],"v":[27047]},{"k":[1654304400],"v":[26707]},{"k":[1654308000],"v":[25248]},{"k":[1654311600],"v":[25142]},{"k":[1654315200],"v":[24997]},{"k":[1654318800],"v":[25009]},{"k":[1654322400],"v":[25831]},{"k":[1654326000],"v":[25825]},{"k":[1654329600],"v":[32478]},{"k":[1654333200],"v":[43094]},{"k":[1654336800],"v":[41610]},{"k":[1654340400],"v":[38198]},{"k":[1654344000],"v":[45737]},{"k":[1654347600],"v":[45705]},{"k":[1654351200],"v":[45722]},{"k":[1654354800],"v":[45653]},{"k":[1654358400],"v":[45748]},{"k":[1654362000],"v":[45681]},{"k":[1654365600],"v":[45682]},{"k":[1654369200],"v":[45682]},{"k":[1654372800],"v":[29833]},{"k":[1654376400],"v":[25784]},{"k":[1654380000],"v":[25537]},{"k":[1654383600],"v":[28640]},{"k":[1654387200],"v":[26595]},{"k":[1654390800],"v":[26633]},{"k":[1654394400],"v":[26292]},{"k":[1654398000],"v":[26367]},{"k":[1654401600],"v":[26425]},{"k":[1654405200],"v":[26768]},{"k":[1654408800],"v":[26681]},{"k":[1654412400],"v":[26961]},{"k":[1654416000],"v":[26441]},{"k":[1654419600],"v":[26736]},{"k":[1654423200],"v":[26514]},{"k":[1654426800],"v":[26341]},{"k":[1654430400],"v":[25693]},{"k":[1654434000],"v":[26545]},{"k":[1654437600],"v":[25346]},{"k":[1654441200],"v":[29568]},{"k":[1654444800],"v":[28391]},{"k":[1654448400],"v":[28319]},{"k":[1654452000],"v":[28226]},{"k":[1654455600],"v":[27700]},{"k":[1654459200],"v":[30284]},{"k":[1654462800],"v":[25941]},{"k":[1654466400],"v":[28172]},{"k":[1654470000],"v":[29254]},{"k":[1654473600],"v":[26714]},{"k":[1654477200],"v":[26245]},{"k":[1654480800],"v":[26497]},{"k":[1654484400],"v":[26435]},{"k":[1654488000],"v":[26455]},{"k":[1654491600],"v":[26745]},{"k":[1654495200],"v":[26597]},{"k":[1654498800],"v":[26440]},{"k":[1654502400],"v":[29763]},{"k":[1654506000],"v":[28625]},{"k":[1654509600],"v":[43735]},{"k":[1654513200],"v":[42616]},{"k":[1654516800],"v":[26843]},{"k":[1654520400],"v":[26859]},{"k":[1654524000],"v":[26625]},{"k":[1654527600],"v":[26559]},{"k":[1654531200],"v":[25392]},{"k":[1654534800],"v":[25382]},{"k":[1654538400],"v":[28459]},{"k":[1654542000],"v":[26013]},{"k":[1654545600],"v":[29661]},{"k":[1654549200],"v":[25549]},{"k":[1654552800],"v":[27221]},{"k":[1654556400],"v":[24428]},{"k":[1654560000],"v":[24486]},{"k":[1654563600],"v":[24880]},{"k":[1654567200],"v":[25008]},{"k":[1654570800],"v":[25394]},{"k":[1654574400],"v":[25670]},{"k":[1654578000],"v":[25711]},{"k":[1654581600],"v":[25818]},{"k":[1654585200],"v":[25725]},{"k":[1654588800],"v":[26315]},{"k":[1654592400],"v":[27172]},{"k":[1654596000],"v":[26805]},{"k":[1654599600],"v":[30202]},{"k":[1654603200],"v":[25752]},{"k":[1654606800],"v":[25685]},{"k":[1654610400],"v":[25513]},{"k":[1654614000],"v":[25252]},{"k":[1654617600],"v":[26531]},{"k":[1654621200],"v":[29304]},{"k":[1654624800],"v":[28700]},{"k":[1654628400],"v":[34169]},{"k":[1654632000],"v":[41485]},{"k":[1654635600],"v":[34056]},{"k":[1654639200],"v":[25038]},{"k":[1654642800],"v":[24838]},{"k":[1654646400],"v":[26327]},{"k":[1654650000],"v":[26202]},{"k":[1654653600],"v":[26835]},{"k":[1654657200],"v":[25925]},{"k":[1654660800],"v":[27483]},{"k":[1654664400],"v":[26502]},{"k":[1654668000],"v":[27351]},{"k":[1654671600],"v":[27375]},{"k":[1654675200],"v":[26509]},{"k":[1654678800],"v":[26190]},{"k":[1654682400],"v":[27074]},{"k":[1654686000],"v":[27471]},{"k":[1654689600],"v":[26786]},{"k":[1654693200],"v":[26478]},{"k":[1654696800],"v":[26999]},{"k":[1654700400],"v":[27373]},{"k":[1654704000],"v":[26690]},{"k":[1654707600],"v":[26394]},{"k":[1654711200],"v":[25525]},{"k":[1654714800],"v":[25999]},{"k":[1654718400],"v":[26259]},{"k":[1654722000],"v":[26738]},{"k":[1654725600],"v":[27275]},{"k":[1654729200],"v":[28722]},{"k":[1654732800],"v":[27661]},{"k":[1654736400],"v":[28155]},{"k":[1654740000],"v":[27115]},{"k":[1654743600],"v":[30941]},{"k":[1654747200],"v":[26503]},{"k":[1654750800],"v":[26292]},{"k":[1654754400],"v":[25938]},{"k":[1654758000],"v":[26938]},{"k":[1654761600],"v":[25901]},{"k":[1654765200],"v":[25847]},{"k":[1654776000],"v":[25919]},{"k":[1654779600],"v":[28443]},{"k":[1654783200],"v":[34927]},{"k":[1654786800],"v":[43847]},{"k":[1654790400],"v":[31114]},{"k":[1654794000],"v":[27392]},{"k":[1654797600],"v":[27188]},{"k":[1654801200],"v":[26263]},{"k":[1654804800],"v":[38181]},{"k":[1654808400],"v":[43858]},{"k":[1654812000],"v":[31795]},{"k":[1654815600],"v":[29758]},{"k":[1654819200],"v":[24599]},{"k":[1654822800],"v":[25671]},{"k":[1654826400],"v":[25882]},{"k":[1654830000],"v":[26279]},{"k":[1654833600],"v":[25645]},{"k":[1654837200],"v":[25663]},{"k":[1654840800],"v":[25415]},{"k":[1654844400],"v":[25888]},{"k":[1654848000],"v":[25899]},{"k":[1654851600],"v":[27698]},{"k":[1654855200],"v":[33173]},{"k":[1654858800],"v":[31425]},{"k":[1654862400],"v":[25535]},{"k":[1654866000],"v":[25728]},{"k":[1654869600],"v":[25988]},{"k":[1654873200],"v":[26855]},{"k":[1654876800],"v":[26352]},{"k":[1654880400],"v":[24856]},{"k":[1654884000],"v":[25694]},{"k":[1654887600],"v":[27376]},{"k":[1654891200],"v":[25804]},{"k":[1654894800],"v":[25675]},{"k":[1654898400],"v":[26701]},{"k":[1654902000],"v":[27150]}],"ms":6.418 }' 
    def test_predict_linear_regression(self):       
        result = LinearRegression.predict_next(self.data)
        self.assertEqual(result[0], 27.153409606835478)
    
    def test_predict_pa_regressor(self):       
        result = PARegressor.predict_next(self.data)
        self.assertEqual(result[0], 27.401676825818598)

if __name__ == '__main__':
    unittest.main()
// https://www.mycarpentry.com/stair-calculator.html

const totalRiseIRCMsg = "<span id=\"a\" onclick=\"infoWindow('INFO','mycarpentry.com says','<p><b>FYI:</b> The IRC building code suggests that the total vertical rise (<b>Total Rise [A]</b>) of a flight of stairs must not be greater than <b>151 inches</b> (3835 mm) between floor levels or landings.</p>')\" style=\"color: black; background-color: #D5A813; font-weight: bold; text-align: center; !important\">&nbsp;&nbsp;FYI [?]&nbsp;&nbsp;</span>";
function stairCalc() {
    var t = 0
      , a = 0
      , e = 0
      , l = 0
      , r = 0
      , u = 0
      , c = 0
      , S = 0
      , n = 0;
    t = document.StairCalc.xInput.value,
    a = document.StairCalc.yInput.value,
    e = document.StairCalc.zInput.value,
    l = document.StairCalc.wInput.value;
    let s = document.getElementById("totalRise-el");
    if ((isNaN(t) || t < 12 || t > 500 ? (infoWindow("INFO", "mycarpentry.com says", "<p>The value of <b>Total Rise</b> must be a decimal value between 12 and 500 inches.</p>"),
    clearResultFields(),
    document.getElementsByName("StairCalc").reset(),
    document.getElementsByName("xInput")[0].focus()) : t > 151 ? s.innerHTML = totalRiseIRCMsg : s.innerHTML = "",
    (isNaN(a) || a < 12 || a > 1200) && (infoWindow("INFO", "mycarpentry.com says", "<p><b>Total Run</b> must be a decimal value between 12 and 1200 inches.</p>"),
    clearResultFields(),
    document.getElementsByName("StairCalc").reset(),
    document.getElementsByName("yInput")[0].focus()),
    (isNaN(e) || e < 2 || e > 200) && (infoWindow("INFO", "mycarpentry.com says", "<p><b>Number of Steps</b> must be a decimal value between 2 and 200 inches.</p>"),
    clearResultFields(),
    document.getElementsByName("StairCalc").reset(),
    document.getElementsByName("zInput")[0].focus()),
    (isNaN(l) || l < .5 || l > 4) && (infoWindow("INFO", "mycarpentry.com says", "<p><b>Tread Thickness</b> must be a decimal value between 0.5 and 4 inches.</p>"),
    clearResultFields(),
    document.getElementsByName("StairCalc").reset(),
    document.getElementsByName("wInput")[0].focus())),
    document.getElementById("StairMountStandard-m").checked)
        r = e - 1;
    else {
        if (!document.getElementById("StairMountFlush-m").checked)
            return alert("Error while determining Stringer Mount Type"),
            !1;
        r = e
    }
    u = a / r,
    c = t / e;
    var o = parseFloat(l)
      , C = parseFloat(c);
    if (document.getElementById("StairMountStandard-m").checked)
        S = C + o;
    else {
        if (!document.getElementById("StairMountFlush-m").checked)
            return alert("Error while determining Stringer Mount Type"),
            !1;
        S = o
    }
    n = c - l;
    var v = c.toFixed(2)
      , g = u.toFixed(2)
      , p = n.toFixed(2)
      , h = S.toFixed(2);
    document.StairCalc.stepRun2.value = fraction(a),
    document.StairCalc.stepRun2F.value = document.StairCalc.stepRun2.value,
    document.StairCalc.totalRise2.value = fraction(t),
    document.StairCalc.totalRise2F.value = document.StairCalc.totalRise2.value,
    document.StairCalc.riseHeight.value = fraction(c),
    document.StairCalc.riseHeight2.value = document.StairCalc.riseHeight.value,
    document.StairCalc.riseHeight2F.value = document.StairCalc.riseHeight.value,
    document.StairCalc.runDist.value = fraction(u),
    document.StairCalc.runDist2.value = document.StairCalc.runDist.value,
    document.StairCalc.runDist2F.value = document.StairCalc.runDist.value,
    document.StairCalc.firstStepHeight.value = fraction(n),
    document.StairCalc.firstStepHeight2.value = document.StairCalc.firstStepHeight.value,
    document.StairCalc.firstStepHeight2F.value = document.StairCalc.firstStepHeight.value,
    document.StairCalc.strP.value = fraction(S),
    document.StairCalc.strP2.value = document.StairCalc.strP.value,
    document.StairCalc.treadThickness2.value = fraction(l),
    document.StairCalc.treadThickness2F.value = fraction(l),
    document.StairCalc.totalSteps.value = fraction(r),
    document.StairCalc.totalSteps2.value = document.StairCalc.totalSteps.value,
    document.StairCalc.totalSteps2F.value = document.StairCalc.totalSteps.value,
    document.StairCalc.Text1.value = r,
    document.StairCalc.riseHeightDec.value = v,
    document.StairCalc.runDistDec.value = g,
    document.StairCalc.firstStepHeightDec.value = p,
    document.StairCalc.strDec.value = h;
    var d = 0
      , F = 0;
    if (document.getElementById("StairMountStandard-m").checked)
        mSLD = Math.sqrt((d = c * (e - 2) + n) * d + (F = u * (e - 1)) * F);
    else {
        if (!document.getElementById("StairMountFlush-m").checked)
            return alert("Error while determining Stringer Mount Type"),
            !1;
        mSLD = Math.sqrt((d = c * (e - 1) + n) * d + (F = u * e) * F)
    }
    mStrLthFrac = fraction(mStrLthDec = mSLD.toFixed(2)),
    document.StairCalc.mStringerLength.value = mStrLthFrac,
    document.StairCalc.mStringerLengthDec.value = mStrLthDec,
    mangleX = 180 * (matanX = Math.atan(mtanX = c / u)) / Math.PI,
    document.StairCalc.mAngle.value = mangleX.toFixed(1)
}
function clearStairFields() {
    document.StairCalc.xInput.value = "",
    document.StairCalc.yInput.value = "",
    document.StairCalc.zInput.value = "",
    document.StairCalc.wInput.value = "",
    document.StairCalc.riseHeight.value = "",
    document.StairCalc.runDist.value = "",
    document.StairCalc.firstStepHeight.value = "",
    document.StairCalc.strP.value = "",
    document.StairCalc.totalSteps.value = "",
    document.StairCalc.Text1.value = "",
    document.StairCalc.riseHeightDec.value = "",
    document.StairCalc.runDistDec.value = "",
    document.StairCalc.firstStepHeightDec.value = "",
    document.StairCalc.strDec.value = "",
    document.StairCalc.stepRun2.value = "",
    document.StairCalc.totalRise2.value = "",
    document.StairCalc.riseHeight2.value = "",
    document.StairCalc.runDist2.value = "",
    document.StairCalc.firstStepHeight2.value = "",
    document.StairCalc.strP2.value = "",
    document.StairCalc.totalSteps2.value = "",
    document.StairCalc.stepRun2F.value = "",
    document.StairCalc.totalRise2F.value = "",
    document.StairCalc.riseHeight2F.value = "",
    document.StairCalc.runDist2F.value = "",
    document.StairCalc.firstStepHeight2F.value = "",
    document.StairCalc.totalSteps2F.value = "",
    document.StairCalc.mStringerLength.value = "",
    document.StairCalc.mStringerLengthDec.value = "",
    document.StairCalc.mAngle.value = "",
    document.StairCalc.treadThickness2.value = "",
    document.StairCalc.treadThickness2F.value = "",
    document.getElementsByName("xInput")[0].setAttribute("class", " field-normal"),
    document.getElementsByName("warningMessage")[0].setAttribute("class", " clearWarningMessage")
}
function clearResultFields() {
    document.StairCalc.riseHeight.value = "",
    document.StairCalc.runDist.value = "",
    document.StairCalc.firstStepHeight.value = "",
    document.StairCalc.strP.value = "",
    document.StairCalc.totalSteps.value = "",
    document.StairCalc.Text1.value = "",
    document.StairCalc.riseHeightDec.value = "",
    document.StairCalc.runDistDec.value = "",
    document.StairCalc.firstStepHeightDec.value = "",
    document.StairCalc.strDec.value = "",
    document.StairCalc.stepRun2.value = "",
    document.StairCalc.totalRise2.value = "",
    document.StairCalc.riseHeight2.value = "",
    document.StairCalc.runDist2.value = "",
    document.StairCalc.firstStepHeight2.value = "",
    document.StairCalc.strP2.value = "",
    document.StairCalc.totalSteps2.value = "",
    document.StairCalc.stepRun2F.value = "",
    document.StairCalc.totalRise2F.value = "",
    document.StairCalc.riseHeight2F.value = "",
    document.StairCalc.runDist2F.value = "",
    document.StairCalc.firstStepHeight2F.value = "",
    document.StairCalc.totalSteps2F.value = "",
    document.StairCalc.mStringerLength.value = "",
    document.StairCalc.mStringerLengthDec.value = "",
    document.StairCalc.mAngle.value = "",
    document.StairCalc.treadThickness2.value = "",
    document.StairCalc.treadThickness2F.value = "",
    document.getElementsByName("warningMessage")[0].setAttribute("class", " clearWarningMessage")
}
function fraction(t) {
    if (whole = String(decimal = t).split(".")[0],
    !(decimal = parseFloat("." + String(decimal).split(".")[1])) || decimal < .032)
        decimal = 0;
    else if (decimal > .968)
        decimal = 0,
        whole++;
    else
        for (decimal *= num = 16,
        decimal = Math.round(decimal); decimal % 2 == 0; )
            decimal /= 2,
            num /= 2;
    return (0 == whole ? "" : whole + "  ") + (0 == decimal ? "" : decimal + "/" + num)
}
function Fractionize(t, a) {
    if (whole = String(decimal = t).split(".")[0],
    !(decimal = parseFloat("." + String(decimal).split(".")[1])) || decimal < .032)
        decimal = 0;
    else if (decimal > .968)
        decimal = 0,
        whole++;
    else {
        decimal *= num = a,
        decimal = Math.round(decimal);
        var e = [11, 7, 5, 3, 2]
          , l = e.length;
        for (i = 0; i < l; i++)
            for (; decimal % e[i] == 0 && num % e[i] == 0; )
                decimal /= e[i],
                num /= e[i]
    }
    return (0 == whole ? "" : whole + "  ") + (0 == decimal ? "" : decimal + "/" + num)
}
function AutoCalcStairRise() {
    var t = 0
      , a = 0
      , e = 0
      , l = 0
      , r = 0
      , u = 0
      , c = 0
      , S = 0
      , n = 0
      , s = 0
      , o = 0
      , C = 0
      , v = 0
      , g = 0
      , p = 0
      , h = 0
      , d = 0
      , F = 0
      , m = 0
      , f = 0;
    v = document.AutoStairCalc.OptStairHeight.value,
    s = Fractionize(g = document.AutoStairCalc.TotalHeightInput.value, 16),
    document.AutoStairCalc.TotalHeight2.value = s,
    document.AutoStairCalc.TotalHeight2F.value = s,
    p = 2 * v;
    let $ = document.getElementById("totalHeight-el");
    if (isNaN(g) || g < 12 || g > 500)
        infoWindow("INFO", "mycarpentry.com says", "<p>The value of <b>Total Rise</b> must be a decimal value between 12 and 500 inches.</p>"),
        AutoClearStairRise();
    else {
        if (g > 151 ? $.innerHTML = totalRiseIRCMsg : $.innerHTML = "",
        x = 1 * (C = String(o = t = (g / v).toFixed(1)).split(".")[0]),
        m = g / (numSteps = (o = parseFloat("." + String(o).split(".")[1])) >= .5 ? a = x + 1 : x),
        document.AutoStairCalc.NumberOfSteps.value = numSteps,
        document.getElementById("StairMountStandard").checked)
            document.AutoStairCalc.NumberOfStringerSteps.value = numSteps - 1,
            document.AutoStairCalc.NumberOfStringerSteps2.value = numSteps - 1;
        else {
            if (!document.getElementById("StairMountFlush").checked)
                return alert("Error while determining Stringer Mount Type"),
                !1;
            document.AutoStairCalc.NumberOfStringerSteps.value = numSteps,
            document.AutoStairCalc.NumberOfStringerSteps2F.value = numSteps
        }
        if (t = m.toFixed(2),
        document.AutoStairCalc.autoCalcStairResultDec.value = t,
        x = Fractionize(t, 16),
        document.AutoStairCalc.autoCalcStairResultFrac.value = x,
        document.AutoStairCalc.autoCalcStairResultFrac2.value = x,
        document.AutoStairCalc.autoCalcStairResultFrac2F.value = x,
        l = (h = m - (d = document.AutoStairCalc.OptTreadThickness.value)).toFixed(2),
        document.AutoStairCalc.firstStepHeightDec.value = l,
        e = Fractionize(l, 16),
        document.AutoStairCalc.firstStepHeightFrac.value = e,
        document.AutoStairCalc.firstStepHeightFrac2.value = e,
        document.AutoStairCalc.firstStepHeightFrac2F.value = e,
        document.AutoStairCalc.TreadThickness2.value = Fractionize(d, 16),
        document.AutoStairCalc.TreadThickness2F.value = document.AutoStairCalc.TreadThickness2.value,
        document.getElementById("StairMountStandard").checked)
            u = (F = 1 * m + 1 * d).toFixed(2),
            document.AutoStairCalc.lastStepDec.value = u,
            r = Fractionize(u, 16);
        else {
            if (!document.getElementById("StairMountFlush").checked)
                return alert("Error while determining Stringer Mount Type"),
                !1;
            u = (F = 1 * d).toFixed(2),
            document.AutoStairCalc.lastStepDec.value = u,
            r = Fractionize(u, 16)
        }
        if (document.AutoStairCalc.lastStepFrac.value = r,
        document.AutoStairCalc.lastStepFrac2.value = r,
        document.AutoStairCalc.lastStepFrac2F.value = r,
        n = Fractionize(f = document.AutoStairCalc.OptTreadDepth.value, 16),
        document.AutoStairCalc.OptTreadDepth2.value = n,
        document.AutoStairCalc.OptTreadDepth2F.value = n,
        c = (TotalRun = (numSteps - 1) * f).toFixed(2),
        document.AutoStairCalc.totalRunDec.value = c,
        S = Fractionize(c, 16),
        document.getElementById("StairMountStandard").checked)
            c = (TotalRun = (numSteps - 1) * f).toFixed(2),
            document.AutoStairCalc.totalRunDec.value = c,
            S = Fractionize(c, 16);
        else {
            if (!document.getElementById("StairMountFlush").checked)
                return alert("Error while determining Stringer Mount Type"),
                !1;
            c = (TotalRun = numSteps * f).toFixed(2),
            document.AutoStairCalc.totalRunDec.value = c,
            S = Fractionize(c, 16)
        }
        document.AutoStairCalc.totalRunFrac.value = S,
        document.AutoStairCalc.totalRunFrac2.value = S,
        document.AutoStairCalc.totalRunFrac2F.value = S;
        var A = 0
          , _ = 0;
        if (document.getElementById("StairMountStandard").checked)
            sLD = Math.sqrt((A = m * (numSteps - 2) + h) * A + (_ = f * (numSteps - 1)) * _);
        else {
            if (!document.getElementById("StairMountFlush").checked)
                return alert("Error while determining Stringer Mount Type"),
                !1;
            sLD = Math.sqrt((A = m * (numSteps - 1) + h) * A + (_ = f * numSteps) * _)
        }
        strLthFrac = Fractionize(strLthDec = sLD.toFixed(2), 16),
        document.AutoStairCalc.stringerLengthFrac.value = strLthFrac,
        document.AutoStairCalc.stringerLengthDec.value = strLthDec,
        angleX = 180 * (atanX = Math.atan(tanX = m / f)) / Math.PI,
        document.AutoStairCalc.railAngleDec.value = angleX.toFixed(1)
    }
}
function AutoClearStairRise() {
    document.AutoStairCalc.autoCalcStairResultDec.value = "",
    document.AutoStairCalc.autoCalcStairResultFrac.value = "",
    document.AutoStairCalc.NumberOfSteps.value = "",
    document.AutoStairCalc.NumberOfStringerSteps.value = "",
    document.AutoStairCalc.TotalHeightInput.value = "",
    document.AutoStairCalc.totalRunFrac.value = "",
    document.AutoStairCalc.totalRunDec.value = "",
    document.AutoStairCalc.lastStepFrac.value = "",
    document.AutoStairCalc.lastStepDec.value = "",
    document.AutoStairCalc.firstStepHeightDec.value = "",
    document.AutoStairCalc.firstStepHeightFrac.value = "",
    document.AutoStairCalc.NumberOfStringerSteps2.value = "",
    document.AutoStairCalc.autoCalcStairResultFrac2.value = "",
    document.AutoStairCalc.firstStepHeightFrac2.value = "",
    document.AutoStairCalc.lastStepFrac2.value = "",
    document.AutoStairCalc.totalRunFrac2.value = "",
    document.AutoStairCalc.TotalHeight2.value = "",
    document.AutoStairCalc.OptTreadDepth2.value = "",
    document.AutoStairCalc.stringerLengthFrac.value = "",
    document.AutoStairCalc.stringerLengthDec.value = "",
    document.AutoStairCalc.railAngleDec.value = "",
    document.AutoStairCalc.NumberOfStringerSteps2F.value = "",
    document.AutoStairCalc.autoCalcStairResultFrac2F.value = "",
    document.AutoStairCalc.firstStepHeightFrac2F.value = "",
    document.AutoStairCalc.lastStepFrac2F.value = "",
    document.AutoStairCalc.totalRunFrac2F.value = "",
    document.AutoStairCalc.TotalHeight2F.value = "",
    document.AutoStairCalc.OptTreadDepth2F.value = "",
    document.AutoStairCalc.TreadThickness2.value = "",
    document.AutoStairCalc.TreadThickness2F.value = "",
    TotalHeight = "",
    MinHeight = ""
}
function ResetDefaults() {
    document.AutoStairCalc.OptStairHeight.value = 7,
    document.AutoStairCalc.OptTreadThickness.value = 1.5,
    document.AutoStairCalc.OptTreadDepth.value = 10.5
}

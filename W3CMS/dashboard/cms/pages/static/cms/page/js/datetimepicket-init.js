/* =================== XdSoft Datetimepicker Start ============================= */
function dateTime() {

    if(jQuery('.FullDateTimePicker').length > 0)
    {
        jQuery('.FullDateTimePicker').datetimepicker({
            format: 'Y-m-d H:i:s',
        });
    }

    if(jQuery('.datetimepicker').length > 0)
    {
        jQuery('.datetimepicker').datetimepicker({
            timepicker: false,
            format: 'Y-m-d',
        });
    }
    
}

function projectStartDate(min_date) {

    newDefaultDate = new Date(min_date);
    newDefaultDate.setMinutes(newDefaultDate.getMinutes() + 1);

    $('#ProjectStartDate').datetimepicker({
        format: 'Y-m-d H:i:s',
        formatTime: 'H:i:s',
        validateOnBlur: false,
        defaultDate: newDefaultDate,
        //minDate: min_date,
        onSelectDate: function ($ct, $i) {
            $('#ProjectEndDate').val('');
            projectEndDate($ct);
        }
    });
}

function projectEndDate(min_date) {

    newDefaultDate = new Date(min_date);
    newDefaultDate.setMinutes(newDefaultDate.getMinutes() + 1);

    $('#ProjectEndDate').datetimepicker({
        format: 'Y-m-d H:i:s',
        formatTime: 'H:i:s',            
        defaultDate: newDefaultDate,
        //minDate: min_date,
        onSelectDate: function ($ct, $i) {
            $('#ProjectLaunchDate').val('');
            projectLaunchDate($ct);
        }
    });
}

function projectLaunchDate(min_date) {

    newDefaultDate = new Date(min_date);
    newDefaultDate.setMinutes(newDefaultDate.getMinutes() + 1);

    $('#ProjectLaunchDate').datetimepicker({
        format: 'Y-m-d H:i:s',
        formatTime: 'H:i:s',            
        defaultDate: newDefaultDate,
        //minDate: min_date
    });
}

function projectInvestmentStartDate(startDate, endDate) {
    $('.ProjectInvestmentSDate').datetimepicker({
        format: 'Y-m-d H:i:s',
        formatTime: 'H:i:s',            
        defaultDate: startDate,
        //minDate: startDate,
        //maxDate: endDate,
        onSelectDate: function ($ct, $i) {
            $i.closest('form').find('.ProjectInvestmentEDate').val('');
            var element = $i.attr('data-endDateField');
            projectInvestmentEndDate(element, $ct, endDate);
        }
    });
}

function projectInvestmentEndDate(element, minDateE, endDateE) {
    newDefaultDate = new Date(minDateE);
    newDefaultDate.setDate(newDefaultDate.getDate() + 1);

    $(element).datetimepicker('destroy');
    $(element).datetimepicker({
        format: 'Y-m-d H:i:s',
        formatTime: 'H:i:s',            
        defaultDate: newDefaultDate,
        //minDate: minDateE,
        //maxDate: endDateE,
    });
}
/* =================== XdSoft Datetimepicker End ============================= */

/* =================== InvestorManagement Module XdSoft Datetimepicker Start ============================= */
dateTime();

if(jQuery('#ProjectStartDate').length > 0 && jQuery('#ProjectEndDate').length > 0 && jQuery('#ProjectLaunchDate').length > 0)
{
    var min_date = new Date();
    var eDate = jQuery('#ProjectStartDate').val() ? jQuery('#ProjectStartDate').val() : min_date;
    var lDate = jQuery('#ProjectEndDate').val() ? jQuery('#ProjectEndDate').val() : min_date;
    projectStartDate(min_date);
    projectEndDate(eDate);
    projectLaunchDate(lDate);
}

if(jQuery('.ProjectInvestmentSDate').length > 0 && jQuery('.ProjectInvestmentEDate').length > 0)
{
    var projectStartDate = jQuery('#ProjectStartDate').val();
    var projectEndDate = jQuery('#ProjectEndDate').val();
    var element = jQuery('.ProjectInvestmentEDate');
    projectInvestmentStartDate(projectStartDate, projectEndDate);
    projectInvestmentEndDate(element, projectStartDate, projectEndDate);
}
/* =================== InvestorManagement Module XdSoft Datetimepicker End ============================= */
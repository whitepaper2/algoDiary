-- drop  table tdl_aopeng_20210301_0909_dt;
create table tdl_aopeng_20210301_0909_dt as
select 
        t1.orderNo,
        t1.transId,
        t1.eventOccurTime,
        FROM_UNIXTIME(substr(t1.eventOccurTime,0,10), 'yyyyMMdd') as eventOccurTime2,
        t1.accountName,
        -- t1.phoneCodeNumber,
        t1.phoneCode,
        t1.accountMobile,
        -- t1.accountAge,
        t1.accountEmail,
        -- t1.registerTime,
        t1.merchandiseName,
        -- regexp_replace(NVL(t1.category1,''),'[\\s]+|[\\u3000]+|[\\s]','') as category1,
        t1.oderItemCount,
        t1.skuNumber,
        -- t1.skuCountMax,
        -- t1.CPFnumber,
        t1.billingPhoneNumber,
        t1.billingCity,
        t1.billingCountry,
        t1.billingState,
        t1.billingZipCode,
        t1.billingAddress,
        t1.billingEmail,
        t1.shippingEmail,
        t1.shippingCountry,
        t1.shippingAddress,
        t1.shippingState,
        t1.shippingCity,
        t1.shippingZipCode,
        t1.payTotalAmount,
        t1.payAmount,
        t1.logisticsFee,
        t1.cardType,
        -- t1.isInstallment,
        -- t1.installmentCount,
        t1.currencyType,
        t1.cardBin,
        t1.isoa2,
        -- t1.deviceType,
        -- t1.orderMode,
        t1.deviceId,
        t1.paymentMethod,
        t1.cardNumber,
        t1.cardBrand,
        t1.cardCategory,
        -- t1.isCardNumberCopy,
        -- t1.isCardScan,
        t1.ipAddress,
        t1.ip2,
        t1.ip3,
        t1.ipAddressCountryCode,
        t1.ipAddressCountry,
        t1.ipProvince,
        t1.ipAddressCity,
        t1.trueipaddresscountrycode,
        t1.trueipaddressprovince,
        t1.trueipaddresscity,
        t1.logisticsType,
        t1.isCouponUsed,
        t1.isLogisticsInsurance,
        t1.finalDecision,
        t1.modelScore,
        t1.rulename,
        t1.paymentResult,
        t1.emailrandomrate,
        t1.websitesource,
        t2.chargebackReason,
        t2.chargebacktime,
        t2.chargebackamount,
        t2.ischargeback,
        t3.chargebackReason2
        
    from 
    (select * from usaep.raw_uskp_data_activity_dt 
    where ds>=20210301 and ds<=20210909 and partnercode="TDAPProject" and eventid="Payment_web_20201022" and transId<>"") t1
    left join
    (select transId,chargebackReason,chargebacktime,1 as ischargeback,chargebackamount from usaep.raw_uskp_data_activity_dt 
    where ds>=20210301 and ds<=20210909 and partnercode="TDAPProject" and eventid="Chargeback_web") t2
    on t1.transId=t2.transId
    left join
    (select transId,chargebackReason2 from
        (select trans_id as transId,regexp_replace(chargeback_reason,"\n","") as chargebackReason2,row_number() over (partition by trans_id order by ds desc) as rowid from usaep.dwb_model_blk_sample_wash_dt 
            where ds>=20210301 and ds<=20210909 and partner_code="TDAPProject") tblk
        where tblk.rowid=1) t3
    on t1.transId=t3.transId;
    

package org.openrdf.sail.generaldb.algebra;

import java.util.ArrayList;

import org.openrdf.sail.generaldb.algebra.base.BinaryGeneralDBOperator;
import org.openrdf.sail.generaldb.algebra.base.GeneralDBQueryModelVisitorBase;
import org.openrdf.sail.generaldb.algebra.base.GeneralDBSqlExpr;
import org.openrdf.sail.generaldb.algebra.base.UnaryGeneralDBOperator;

public class GeneralDBSqlSpatialMetricUnary extends UnaryGeneralDBOperator
{
	

	/*CONSTRUCTOR*/
	
	public GeneralDBSqlSpatialMetricUnary(GeneralDBSqlExpr expr) {
		super(expr);
	}

	@Override
	public <X extends Exception> void visit(GeneralDBQueryModelVisitorBase<X> visitor)
		throws X
	{
		visitor.meet(this);
	}

}